// Runs after the page DOM is ready, so elements exist
document.addEventListener("DOMContentLoaded", () => {
  // Enables tag-style multiselect for reference types: users can pick multiple types,
  // search options, and remove selected ones with an “x” (Choices.js)
  const typesSelect = document.getElementById("types");
  if (typesSelect) {
    new Choices(typesSelect, {
      removeItemButton: true,
      placeholder: true,
      placeholderValue: 'Select types',
      searchPlaceholderValue: 'Search type',
      shouldSort: true,
    });
  }

  // References to the container that holds filter rows and the button that adds new rows
  const fieldFiltersContainer = document.getElementById("field-filters");
  const addFilterBtn = document.getElementById("add-field-filter");

  // Builds <option> list for the field dropdown from server-provided JSON (data-all-fields)
  function buildOptionsHtmlFromData() {
    const data = fieldFiltersContainer.dataset.allFields;
    if (!data) return "";
    try {
      const fields = JSON.parse(data);
      return fields.map(f => `<option value="${f}">${f}</option>`).join("");
    } catch (e) {
      console.error("Failed to parse all_fields:", e);
      return "";
    }
  }

  // Gets field dropdown options: reuse existing row’s options if present, otherwise generate from JSON data
  function getAllFieldOptionsHtml() {
    const existingSelect = fieldFiltersContainer.querySelector('select[name="field[]"]');
    if (existingSelect) return existingSelect.innerHTML;
    return buildOptionsHtmlFromData();
  }

  // Creates one filter row: field selector + operator selector + value input + remove button
  function createFilterRow(allFieldOptionsHtml) {
    const row = document.createElement("div");
    row.className = "filter-row";
    row.innerHTML = `
      <select name="field[]">
        ${allFieldOptionsHtml}
      </select>
      <select name="op[]">
        <option value="contains">contains</option>
        <option value="equals">equals</option>
        <option value="startswith">startswith</option>
        <option value="endswith">endswith</option>
      </select>
      <input type="text" name="value[]" placeholder="Value">
      <button type="button" class="remove-filter" aria-label="Remove filter">&times;</button>
    `;
    // Removes this filter row when the user clicks the “×” button
    row.querySelector(".remove-filter").addEventListener("click", () => {
      row.remove();
    });
    return row;
  }

  // Adds a new filter row when the user clicks “Add field filter”; warns if field list is unavailable
  if (addFilterBtn) {
    addFilterBtn.addEventListener("click", () => {
      const html = getAllFieldOptionsHtml();
      if (!html) {
        alert("Field list is not available.");
        return;
      }
      fieldFiltersContainer.appendChild(createFilterRow(html));
    });
  }
});
