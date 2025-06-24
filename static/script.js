document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("uploadForm");
    const loading = document.getElementById("loading");

    form.addEventListener("submit", function () {
        loading.classList.remove("hidden");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("uploadForm");
    const loading = document.getElementById("loading");
    const toggle = document.getElementById("darkModeToggle");

    // Show loading
    form.addEventListener("submit", function () {
        loading.classList.remove("hidden");
    });

    // Toggle dark mode
    toggle.addEventListener("change", function () {
        document.body.classList.toggle("dark", this.checked);
        localStorage.setItem("darkMode", this.checked ? "on" : "off");
    });

    // Load saved mode
    const saved = localStorage.getItem("darkMode");
    if (saved === "on") {
        toggle.checked = true;
        document.body.classList.add("dark");
    }
});

