// event listener for changing reference type
const refTypeSelect = document.querySelector("#ref-type-input");

refTypeSelect.addEventListener("change", () => {
    const refTypes = refTypeSelect.children;
    const selectedOption = refTypes[refTypeSelect.selectedIndex].value;
    document.location.replace(`/new-reference?type=${selectedOption}`);
  },
  true
);

// event listener for adding fields
const addBtn = document.querySelector("#add-field-button");
const fieldSelect = document.querySelector("#field-select");
const fields = document.querySelector("#fields");
const fieldAdder = document.querySelector("#field-adder")

addBtn.addEventListener("click", () => {
  // get selected field type and value
  const selectedField = fieldSelect.children[fieldSelect.selectedIndex];
  const fieldType = selectedField.value;

  // create label for new field type
  const label = document.createElement("label");
  label.textContent = fieldType;
  label.htmlFor = fieldType;

  // create textarea for new field type
  const textarea = document.createElement("textarea");
  textarea.name = fieldType;
  textarea.id = fieldType;
  textarea.classList = ["field-value input-select"]
  textarea.rows = 1;
  textarea.maxLength = 500;

  // append label and textarea to fields
  fields.appendChild(label);
  fields.appendChild(textarea);

  // delete selected optional field type
  fieldSelect.removeChild(selectedField);

  // remove the select-element if no more optional fields can be added
  if (fieldSelect.children.length === 0) {
    fieldAdder.remove();
  }
});
