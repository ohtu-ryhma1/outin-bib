// Export copy clipboard handling
document.querySelector("#copy-export-button").addEventListener("click", function () {
  const textarea = document.querySelector("#export-textarea");
  const text = textarea.value;
  navigator.clipboard.writeText(text)
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
