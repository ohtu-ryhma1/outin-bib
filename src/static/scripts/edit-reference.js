// remove the select-element if no there are no optional fields
const optionalSelect = document.querySelector("#field-select");

if (optionalSelect.children.length === 0) {
  document.querySelector("#field-adder").remove();
}

// event listener for adding fields
const addBtn = document.querySelector("#add-field");
addBtn.addEventListener("click", () => {
  // get selected field type
  const optionalSelect = document.querySelector("#field-select");
  const field = optionalSelect.children[optionalSelect.selectedIndex];
  const fieldType = field.value;

  // create label for new field type
  const label = document.createElement("label");
  label.textContent = fieldType;
  label.htmlFor = fieldType;

  // create textarea for new field type
  const textarea = document.createElement("textarea");
  textarea.name = fieldType;
  textarea.id = fieldType;
  textarea.classList = ["field-value"]
  textarea.rows = 1;
  textarea.maxLength = 500;

  // append label and textarea to document
  const optionalFieldsContainer = document.querySelector("#fields");
  optionalFieldsContainer.appendChild(label);
  optionalFieldsContainer.appendChild(textarea);

  // delete selected optional field type
  optionalSelect.removeChild(field);

  // remove the select-element if no more optional fields can be added
  if (optionalSelect.children.length === 0) {
    document.querySelector("#field-adder").remove();
  }
});
