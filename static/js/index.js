document.addEventListener('DOMContentLoaded', function () {
    const urlInput = document.querySelector('.url-input');
    const shortenBtn = document.querySelector('.shorten-btn');
    const result = document.querySelector('.result');
    const resultDisplay = document.querySelector('.result-display');
    const copyBtn = document.querySelector('.copy-btn');

    urlInput.addEventListener('input', function () {
        try {
            new URL(this.value);
            shortenBtn.disabled = false;
            result.classList.remove('active');
        } catch {
            shortenBtn.disabled = true;
            result.classList.remove('active');
        }
    });

    shortenBtn.addEventListener('click', async function () {
        if (!urlInput.value) return;

        const endpoint = `/generate?url=${encodeURIComponent(urlInput.value)}`;

        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'accept': 'application/json',
            },
            body: '',
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Something went wrong');
        }

        const shortUrl = await response.text();
        resultDisplay.value = shortUrl.slice(1, -1);
        result.classList.add('active');
    });

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
