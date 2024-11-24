document.addEventListener('DOMContentLoaded', function() {
  const urlInput = document.querySelector('.url-input');
  const shortenBtn = document.querySelector('.shorten-btn');
  const result = document.querySelector('.result');
  const resultDisplay = document.querySelector('.result-display');
  const copyBtn = document.querySelector('.copy-btn');

  shortenBtn.addEventListener('click', function() {
    if (!urlInput.value) {
      alert('Please enter a URL');
      return;
    }

    // Simulating API call
    const randomString = Math.random().toString(36).substring(7);
    const shortUrl = `https://short.link/${randomString}`;

    resultDisplay.value = shortUrl;
    result.classList.add('active');
  });

  copyBtn.addEventListener('click', function() {
    resultDisplay.select();
    navigator.clipboard.writeText(resultDisplay.value).then(function() {
      const originalText = copyBtn.innerHTML;
      copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
      setTimeout(() => {
        copyBtn.innerHTML = originalText;
      }, 2000);
    });
  });

  // Add input validation
  urlInput.addEventListener('input', function() {
    try {
      new URL(this.value);
      shortenBtn.disabled = false;
    } catch {
      shortenBtn.disabled = true;
    }
  });
});