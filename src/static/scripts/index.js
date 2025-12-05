const searchOverlay = document.querySelector("#search-overlay");

// toggle the search window via the search button
const searchButton = document.querySelector("#open-search-button");
searchButton.addEventListener("click", () => {
  searchOverlay.classList.toggle("active");
});

// close the search window via the close button
const closeButton = document.querySelector("#close-search-button");
closeButton.addEventListener("click", () => {
  searchOverlay.classList.toggle("active");
});

// create Choises object for reference type filter
const refTypesSelect = document.querySelector("#ref-type");
new Choices(refTypesSelect, {
  placeholder: true,
  placeholderValue: "Select types",
  removeItemButton: true,
  searchPlaceholderValue: "Search type",
  shouldSort: true,
});

const fieldFilters = document.querySelector("#field-filters");

// add a new filter
const addFilterBtn = document.querySelector("#add-filter-button");
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
        <input type="text" name="field-value" placeholder="value">
        <button type="button" class="remove-filter-button">
            <span class="remove-filter-icon material-symbols-outlined">close</span>
        </button>`;

  // remove this field when the remove button is clicked
  filterDiv
    .querySelector(".remove-filter-button")
    .addEventListener("click", () => {
      filterDiv.remove();
    });

  // add the field to the DOM
  fieldFilters.appendChild(filterDiv);
});

// add remove button functionality to existing filters
const existingButtons = document.querySelectorAll(".remove-filter-button")
existingButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    btn.parentElement.remove()
  })
})