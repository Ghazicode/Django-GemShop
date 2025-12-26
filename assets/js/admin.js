document.addEventListener('DOMContentLoaded', function() {
    const generateDescriptionBtn = document.getElementById('generateDescriptionBtn');
    const productNameInput = document.getElementById('productName');
    const gameNameInput = document.getElementById('gameName');
    const quantityInput = document.getElementById('quantity');
    const initialDescriptionInput = document.getElementById('initialDescription');
    const generatedDescriptionOutput = document.getElementById('generatedDescription');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const errorAlert = document.getElementById('errorAlert');
    const copyDescriptionBtn = document.getElementById('copyDescriptionBtn');
    const copySuccessAlert = document.getElementById('copySuccessAlert');

    // Function to show alert messages temporarily
    function showAlert(element, displayTime = 2000) {
        element.style.display = 'block';
        setTimeout(() => {
            element.style.display = 'none';
        }, displayTime);
    }

    // Event listener for the Generate Description button
    if (generateDescriptionBtn) {
        generateDescriptionBtn.addEventListener('click', async function(event) {
            event.preventDefault(); // Prevent default form submission

            // Hide previous outputs/alerts
            generatedDescriptionOutput.value = '';
            document.getElementById('generatedDescriptionOutput').style.display = 'none';
            errorAlert.style.display = 'none';
            copySuccessAlert.style.display = 'none';

            // Get input values
            const productName = productNameInput.value.trim();
            const gameName = gameNameInput.value.trim();
            const quantity = quantityInput.value.trim();
            const initialDescription = initialDescriptionInput.value.trim();

            if (!productName || !gameName) {
                errorAlert.textContent = 'لطفاً نام محصول و نام بازی را وارد کنید.';
                showAlert(errorAlert, 3000);
                return;
            }

            // Show loading indicator
            loadingIndicator.style.display = 'block';
            generateDescriptionBtn.disabled = true; // Disable button during loading

            // Construct the prompt for the LLM
            let chatHistory = [];
            let prompt = `یک توضیح محصول جذاب و کامل برای فروش آنلاین بنویس. این محصول برای فروش در یک وبسایت فروش جم و آیتم‌های بازی است.
            نام محصول: ${productName}
            نام بازی: ${gameName}`;
            if (quantity) {
                prompt += `
            مقدار: ${quantity}`;
            }
            if (initialDescription) {
                prompt += `
            توضیحات اولیه/ویژگی‌های خاص: ${initialDescription}`;
            }
            prompt += `
            توضیحات باید شامل مزایای خرید از سایت ما (مثل تحویل فوری، قیمت رقابتی، امنیت) باشد. لحن دوستانه و تشویق‌کننده باشد.`;
            
            chatHistory.push({ role: "user", parts: [{ text: prompt }] });
            const payload = { contents: chatHistory };
            const apiKey = ""; // Canvas will provide this automatically
            const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;

            // Call Gemini API
            try {
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                const result = await response.json();

                if (result.candidates && result.candidates.length > 0 &&
                    result.candidates[0].content && result.candidates[0].content.parts &&
                    result.candidates[0].content.parts.length > 0) {
                    const text = result.candidates[0].content.parts[0].text;
                    generatedDescriptionOutput.value = text;
                    document.getElementById('generatedDescriptionOutput').style.display = 'block';
                } else {
                    errorAlert.textContent = 'پاسخی از هوش مصنوعی دریافت نشد یا ساختار پاسخ نامعتبر بود.';
                    showAlert(errorAlert);
                    console.error('Unexpected API response structure:', result);
                }
            } catch (error) {
                errorAlert.textContent = 'خطا در ارتباط با هوش مصنوعی. لطفا اتصال اینترنت خود را بررسی کنید.';
                showAlert(errorAlert);
                console.error('Error calling Gemini API:', error);
            } finally {
                loadingIndicator.style.display = 'none'; // Hide loading indicator
                generateDescriptionBtn.disabled = false; // Re-enable button
            }
        });
    }

    // Event listener for Copy Description button
    if (copyDescriptionBtn) {
        copyDescriptionBtn.addEventListener('click', function() {
            generatedDescriptionOutput.select();
            document.execCommand('copy'); // Use execCommand for clipboard due to iframe restrictions
            showAlert(copySuccessAlert);
        });
    }
});