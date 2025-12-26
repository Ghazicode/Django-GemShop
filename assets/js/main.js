document.addEventListener('DOMContentLoaded', function() {
    // --- Dark/Light Mode Toggle Logic ---
    const themeToggleBtn = document.getElementById('theme-toggle');
    const body = document.body;

    // Check for saved theme preference on load
    // بررسی ترجیح تم ذخیره شده در هنگام بارگذاری
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        body.classList.add(savedTheme);
        if (savedTheme === 'dark-mode') {
            themeToggleBtn.querySelector('i').classList.replace('fa-sun', 'fa-moon');
        } else {
            themeToggleBtn.querySelector('i').classList.replace('fa-moon', 'fa-sun');
        }
    } else {
        // Default to dark mode if no preference is saved (as per Dracula palette)
        // به طور پیش‌فرض به حالت دارک مود اگر ترجیحی ذخیره نشده باشد
        body.classList.add('dark-mode');
        localStorage.setItem('theme', 'dark-mode');
        themeToggleBtn.querySelector('i').classList.replace('fa-sun', 'fa-moon');
    }

    // Event listener for theme toggle button
    // شنونده رویداد برای دکمه تغییر تم
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', function() {
            if (body.classList.contains('dark-mode')) {
                body.classList.remove('dark-mode');
                body.classList.add('light-mode');
                localStorage.setItem('theme', 'light-mode');
                themeToggleBtn.querySelector('i').classList.replace('fa-moon', 'fa-sun');
            } else {
                body.classList.remove('light-mode');
                body.classList.add('dark-mode');
                localStorage.setItem('theme', 'dark-mode');
                themeToggleBtn.querySelector('i').classList.replace('fa-sun', 'fa-moon');
            }
        });
    }


    // --- Popular Products Carousel Logic ---
    const carouselWrapper = document.querySelector('.popular-products-carousel-wrapper');
    const carousel = document.querySelector('.popular-products-carousel');
    
    // Get all original items to duplicate them for the infinite loop effect
    const originalCarouselItems = carousel.querySelectorAll(':scope > .col'); 

    if (carouselWrapper && carousel && originalCarouselItems.length > 0) {
        // Number of items visible at once (on large screens, col-md-2dot4 = 5 items)
        const itemsToShow = 5; 

        // Duplicate the first 'itemsToShow' number of items and append them to the end
        for (let i = 0; i < itemsToShow; i++) {
            const clonedItem = originalCarouselItems[i].cloneNode(true);
            carousel.appendChild(clonedItem);
        }

        let currentScrollIndex = 0;
        const totalOriginalItems = originalCarouselItems.length;

        // Function to perform the scroll
        function scrollCarousel() {
            currentScrollIndex++;
            const scrollAmount = originalCarouselItems[0].getBoundingClientRect().width;

            carouselWrapper.scrollBy({
                left: scrollAmount, 
                behavior: 'smooth'
            });

            if (currentScrollIndex >= totalOriginalItems) {
                setTimeout(() => {
                    carouselWrapper.scrollTo({
                        left: 0, 
                        behavior: 'auto'
                    });
                    currentScrollIndex = 0;
                }, 600); 
            }
        }

        // Auto-scroll every 3 seconds
        setInterval(scrollCarousel, 3000);
    }
});
