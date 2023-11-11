document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    form.addEventListener("submit", function(e) {
        const locationInput = document.getElementById("location");
        if (!locationInput.value) {
            alert("Please enter a location");
            e.preventDefault(); // Prevent form submission
        }
    });
});