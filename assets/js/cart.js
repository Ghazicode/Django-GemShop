
document.addEventListener('DOMContentLoaded', function() {
    // --- Quantity Adjustment Logic ---
    const quantityInputGroups = document.querySelectorAll('.input-group');

    quantityInputGroups.forEach(group => {
        const minusButton = group.querySelector('.btn-outline-secondary:first-child');
        const plusButton = group.querySelector('.btn-outline-secondary:last-child');
        const quantityInput = group.querySelector('input[type="text"]');

        if (minusButton && plusButton && quantityInput) {
            minusButton.addEventListener('click', function() {
                let currentValue = parseInt(quantityInput.value);
                if (currentValue > 1) {
                    quantityInput.value = currentValue - 1;
                    updateCartTotals();
                }
            });

            plusButton.addEventListener('click', function() {
                let currentValue = parseInt(quantityInput.value);
                quantityInput.value = currentValue + 1;
                updateCartTotals();
            });

            quantityInput.addEventListener('change', function() {
                let currentValue = parseInt(quantityInput.value);
                if (isNaN(currentValue) || currentValue < 1) {
                    quantityInput.value = 1;
                }
                updateCartTotals();
            });
        }
    });

    // --- Item Removal Logic ---
    const deleteButtons = document.querySelectorAll('.cart-item-remove-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const cartItem = button.closest('.d-flex.align-items-center.mb-3.pb-3.border-bottom');
            
            if (cartItem) {
                cartItem.remove();
                console.log("Cart item removed.");
                updateCartTotals();
            }
        });
    });

    // --- Dynamic Input Fields and Active Button State for Login Method ---
    const facebookLoginBtn = document.getElementById('facebookLoginBtn');
    const activisionLoginBtn = document.getElementById('activisionLoginBtn');
    const facebookInputsDiv = document.getElementById('facebookInputs');
    const generalGameInputsDiv = document.getElementById('generalGameInputs');
    const loginMethodButtons = document.querySelectorAll('.btn-outline-primary[id$="LoginBtn"]'); // Selects all buttons ending with LoginBtn

    // Function to toggle input visibility and active button state
    function toggleLoginMethod(selectedMethodBtnId) {
        // Remove active class from all method buttons
        loginMethodButtons.forEach(btn => {
            btn.classList.remove('active-login-method');
        });

        // Add active class to the clicked button
        const selectedBtn = document.getElementById(selectedMethodBtnId);
        if (selectedBtn) {
            selectedBtn.classList.add('active-login-method');
        }

        // Toggle input visibility based on selected method
        if (selectedMethodBtnId === 'facebookLoginBtn') {
            facebookInputsDiv.style.display = 'block';
            generalGameInputsDiv.style.display = 'none';
        } else if (selectedMethodBtnId === 'activisionLoginBtn') {
            facebookInputsDiv.style.display = 'none';
            generalGameInputsDiv.style.display = 'block';
        } else {
            // Default or unknown state
            facebookInputsDiv.style.display = 'none';
            generalGameInputsDiv.style.display = 'block';
        }

        // Adjust required attributes based on visibility
        facebookInputsDiv.querySelectorAll('input').forEach(input => {
            if (selectedMethodBtnId === 'facebookLoginBtn') {
                input.setAttribute('required', 'true');
            } else {
                input.removeAttribute('required');
            }
        });
        generalGameInputsDiv.querySelectorAll('input').forEach(input => {
            if (selectedMethodBtnId === 'activisionLoginBtn') {
                input.setAttribute('required', 'true');
            } else {
                input.removeAttribute('required');
            }
        });
    }

    // Event listeners for login method buttons
    if (facebookLoginBtn) {
        facebookLoginBtn.addEventListener('click', function() {
            toggleLoginMethod('facebookLoginBtn');
        });
    }

    if (activisionLoginBtn) {
        activisionLoginBtn.addEventListener('click', function() {
            toggleLoginMethod('activisionLoginBtn');
        });
    }

    // Initialize input visibility and active button state on page load
    // Set Activision as default selected method
    toggleLoginMethod('activisionLoginBtn');


    // --- Placeholder function for updating cart totals ---
    function updateCartTotals() {
        console.log("Cart totals need to be updated!");
        // Your logic to calculate and update totals here.
    }
});
