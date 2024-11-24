document.addEventListener('DOMContentLoaded', function () {
    const urlInput = document.querySelector('.url-input');
    const shortenBtn = document.querySelector('.shorten-btn');
    const result = document.querySelector('.result');
    const resultDisplay = document.querySelector('.result-display');
    const copyBtn = document.querySelector('.copy-btn');
    const errorMessage = document.querySelector('.error-message');

    // Enable/Disable the button based on URL validity
    urlInput.addEventListener('input', function () {
        try {
            new URL(this.value);
            shortenBtn.disabled = false;
            errorMessage.style.display = 'none';
        } catch {
            shortenBtn.disabled = true;
        }
    });

    // Send POST request to generate short URL
    shortenBtn.addEventListener('click', async function () {
        if (!urlInput.value) return;

        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({url: urlInput.value}),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Something went wrong');
            }

            const shortUrl = await response.text();
            resultDisplay.value = shortUrl;
            result.classList.add('active');
        } catch (err) {
            errorMessage.style.display = 'block';
            errorMessage.textContent = err.message;
        }
    });

    // Copy functionality
    copyBtn.addEventListener('click', function () {
        resultDisplay.select();
        navigator.clipboard.writeText(resultDisplay.value).then(() => {
            const originalText = copyBtn.innerHTML;
            copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
            setTimeout(() => {
                copyBtn.innerHTML = originalText;
            }, 2000);
        });
    });
});