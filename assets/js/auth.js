javascript
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const loginUsernameInput = document.getElementById('loginUsername');
    const loginPasswordInput = document.getElementById('loginPassword');
    const authMessage = document.getElementById('authMessage');

    // Function to show alert messages temporarily
    // تابع برای نمایش موقت پیام‌های هشدار
    function showAlert(element, message, type = 'danger', displayTime = 3000) {
        element.textContent = message;
        element.className = `alert alert-${type} text-center`; // Update class for styling
        element.style.display = 'block';
        setTimeout(() => {
            element.style.display = 'none';
        }, displayTime);
    }

    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission
            // جلوگیری از ارسال پیش‌فرض فرم

            const username = loginUsernameInput.value.trim();
            const password = loginPasswordInput.value.trim();

            // Clear previous messages
            // پاک کردن پیام‌های قبلی
            authMessage.style.display = 'none';

            // --- Authentication Logic ---
            // منطق احراز هویت
            if (username === 'admin' && password === 'admin') {
                // Admin login
                // ورود مدیر
                localStorage.setItem('isLoggedIn', 'true');
                localStorage.setItem('userRole', 'admin'); 
                showAlert(authMessage, 'ورود مدیر موفقیت‌آمیز! در حال انتقال به پنل مدیریت...', 'success', 2000);
                setTimeout(() => {
                    window.location.href = 'admin/manage-products.html'; // Redirect to admin panel
                    // هدایت به پنل مدیریت
                }, 2000);
            } else if (username && password) {
                // Simulate regular user login (any other credentials)
                // شبیه‌سازی ورود کاربر عادی (هر نام کاربری و رمز عبور دیگر)
                localStorage.setItem('isLoggedIn', 'true');
                localStorage.setItem('userRole', 'user'); // Set user role for regular users
                // تنظیم نقش کاربر به "user"
                showAlert(authMessage, 'ورود موفقیت‌آمیز! در حال انتقال به صفحه اصلی...', 'success', 2000);
                setTimeout(() => {
                    window.location.href = 'index.html'; // Redirect to main page for regular users
                    // هدایت به صفحه اصلی برای کاربران عادی
                }, 2000);
            } else {
                // Invalid or empty credentials
                // اطلاعات نامعتبر یا خالی
                showAlert(authMessage, 'نام کاربری یا رمز عبور نمی‌تواند خالی باشد.', 'danger');
            }
        });
    }

    // You can add similar logic for the registration form (registerForm) here if needed
    // در صورت نیاز می‌توانید منطق مشابهی را برای فرم ثبت‌نام (registerForm) در اینجا اضافه کنید.
    // For now, it's just the login functionality.
    // در حال حاضر، فقط قابلیت ورود پیاده‌سازی شده است.
});
