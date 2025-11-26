const optionalBtn = document.getElementById("optional-button")
optionalBtn.addEventListener("click", () => {
    // remove no optionals added texts if there
    const noOptionals = document.getElementById("no-optionals")
    if (noOptionals) {
        noOptionals.remove()
    }
    // get options
    const optionalSelect = document.getElementById("optional-select")
    const selectedOption = optionalSelect.children[optionalSelect.selectedIndex]
    const selectedValue = selectedOption.value

    // create new field
    const fieldDiv = document.createElement("div")

    const label = document.createElement("label")
    label.textContent = selectedValue + ": "
    label.htmlFor = selectedValue

    const input = document.createElement("input")
    input.type = "text"
    input.name = selectedValue
    input.maxLength = 500

    const optionalDiv = document.getElementById("optional-fields")
    fieldDiv.appendChild(label)
    fieldDiv.appendChild(input)
    optionalDiv.appendChild(fieldDiv)

    // delete field
    optionalSelect.removeChild(selectedOption)
    // check if no more options, then remove selection and add appropriate message
    if (optionalSelect.children.length === 0 ) {
        optionalSelect.remove()
        optionalBtn.remove()
        const optionalLabel = document.getElementById("optional-label")
        optionalLabel.innerHTML = "No more optional fields left to be added!"
    }   
})