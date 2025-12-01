// toggle the search window via the search icon
const searchIcon = document.querySelector("#search-icon");
const searchOverlay = document.querySelector("#search-overlay");
searchIcon.addEventListener("click", () => {
  searchOverlay.classList.toggle("active");
});

// create Choises object for reference type filter
const refTypesSelect = document.querySelector("#ref-type");
new Choices(refTypesSelect, {
  removeItemButton: true,
  placeholder: true,
  placeholderValue: "Select types",
  searchPlaceholderValue: "Search type",
  shouldSort: true,
});

const fieldFilters = document.querySelector("#field-filters");

// add a new filter
const addFilterBtn = document.querySelector("#add-field-filter");
addFilterBtn.addEventListener("click", () => {
  const fieldTypes = JSON.parse(fieldFilters.dataset.list)

  // create select element and append the options
  let selectHTML = '<select name="field-type">';
  fieldTypes.forEach(function (field) {
    selectHTML += `<option>${field}</option>`;
  });
  selectHTML += "</select>";

  // construct the rest of the filter element
  const filterDiv = document.createElement("div");
  filterDiv.className = "field-filter";
  filterDiv.innerHTML = `
        ${selectHTML}
        <input type="text" name="field-value" placeholder="Value">
        <button type="button" class="remove-filter-button">
            <span class="material-symbols-outlined">close</span>
        </button>`;

  // remove this field when the remove button is clicked
  filterDiv
    .querySelector(".remove-filter-button")
    .addEventListener("click", () => {
      filterDiv.remove();
    });

  // add the field to the DOM
  document.querySelector("#field-filters").appendChild(filterDiv);
});
