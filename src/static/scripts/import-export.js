// Export copy clipboard handling
document.querySelector("#copy-export-button").addEventListener("click", function () {
  const textarea = document.querySelector("#export-textarea");
  const text = textarea.value;
  const icon = document.querySelector("#copy-export-button .material-symbols-outlined");
  navigator.clipboard.writeText(text)
    .then(() => {
      if (icon) icon.textContent = "check";
      if (window.__copyExportTimeoutId) {
        clearTimeout(window.__copyExportTimeoutId);
        window.__copyExportTimeoutId = null;
      }
      window.__copyExportTimeoutId = setTimeout(() => {
        if (icon) icon.textContent = "content_copy";
        window.__copyExportTimeoutId = null;
      }, 2000);
    })
    .catch(() => {
      if (icon) icon.textContent = "close";
      if (window.__copyExportTimeoutId) {
        clearTimeout(window.__copyExportTimeoutId);
        window.__copyExportTimeoutId = null;
      }
      window.__copyExportTimeoutId = setTimeout(() => {
        if (icon) icon.textContent = "content_copy";
        window.__copyExportTimeoutId = null;
      }, 2000);
    });
});

// Import file hover detection

const dropContainer = document.querySelector("#import-file-container");
const fileInput = document.querySelector("#import-file-input");

dropContainer.addEventListener(
  "dragover",
  (e) => {
    e.preventDefault();
  },
  false
);

dropContainer.addEventListener("dragenter", () => {
  dropContainer.classList.add("drag-active");
});

dropContainer.addEventListener("dragleave", () => {
  dropContainer.classList.remove("drag-active");
});

dropContainer.addEventListener("drop", (e) => {
  e.preventDefault();
  dropContainer.classList.remove("drag-active");
  fileInput.files = e.dataTransfer.files;
});
