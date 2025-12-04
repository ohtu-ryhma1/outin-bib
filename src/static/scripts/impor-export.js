document.addEventListener('DOMContentLoaded', () => {
  const copyBtn = document.getElementById('copy-btn');
  const textarea = document.getElementById('export-textarea');

  fetch('/export-text')
    .then(response => response.text())
    .then(data => {
      textarea.value = data;
    })
    .catch(err => {
      console.error('Failed to fetch exported references:', err);
      textarea.value = 'Error loading exported references';
    });

  copyBtn.addEventListener('click', () => {
    textarea.select();
    document.execCommand('copy');
    alert('Copied to clipboard!');
  });
});
