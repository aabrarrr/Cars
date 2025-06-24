from flask import Flask, render_template, request
from ultralytics import YOLO
import os

app = Flask(__name__)

# Load model YOLO
model = YOLO("best.pt")

# Folder untuk upload dan hasil deteksi
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
PREDICT_FOLDER = os.path.join(RESULT_FOLDER, 'predict')

# Pastikan semua folder ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PREDICT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None

    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = file.filename
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            # Jalankan deteksi
            results = model.predict(
                source=filepath,
                save=True,
                project=RESULT_FOLDER,
                name='predict',
                exist_ok=True
            )

            # Ambil path hasil prediksi
            result_img_path = os.path.join(results[0].save_dir, filename)

            # FIX: path untuk digunakan di HTML (ganti \ jadi /)
            image_url = os.path.join('results', 'predict', filename).replace('\\', '/')

            print("✅ image_url untuk HTML:", image_url)

    return render_template("index.html", image_url=image_url)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
