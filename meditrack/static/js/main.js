
document.addEventListener("DOMContentLoaded", function () {
    // Focus the first field when a form opens.
    const firstInput = document.querySelector(
        ".form-card input, .form-card select"
    );

    if (firstInput) {
        firstInput.focus();
    }

    // Prevent accidental double submission.
    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {
        form.addEventListener("submit", function () {
            const submitButton = form.querySelector(
                'button[type="submit"]'
            );

            if (submitButton) {
                submitButton.disabled = true;
                submitButton.textContent = "Please wait...";
            }
        });
    });
});
