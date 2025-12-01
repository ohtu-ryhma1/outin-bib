*** Settings ***
Documentation    Keywords for using the search/filter modal on the homepage.
...              Existing filters are rendered in the template, and new ones can be
...              added dynamically with the “Add filter” button.

Library          SeleniumLibrary
Resource         ../shared/browser.resource


*** Keywords ***
Open Filter Modal
    # TODO: Replace with actual selector
    Click Element    xpath=//button[@id='open-filter-modal']    # TODO: update
    Wait Until Page Contains Element    id=search-form


Filter By Name
    [Arguments]    ${name}
    Open Filter Modal
    Input Text    id=name    ${name}

    # Submit the form
    Click Button    xpath=//button[@type="submit"]    # TODO: verify selector
    Wait Until Page Contains    ${name}


Select Types
    [Arguments]    @{types}
    Open Filter Modal

    # Choices.js hides the real <select>, so type into search field
    FOR    ${t}    IN    @{types}
        # TODO: Update selectors; Choices.js uses dynamically generated structure.
        # Something like:
        # Click Element   xpath=//div[contains(@class,'choices__inner')]
        # Input Text      xpath=//input[contains(@class,'choices__input')]    ${t}
        # Press Key       xpath=//input[contains(@class,'choices__input')]    ENTER
        Click Element    xpath=//div[@id="types"]    # TODO
        # This must be updated once HTML is final
    END

    Click Button    xpath=//button[@type="submit"]
    Sleep    0.5


Add Field Filter Row
    # Click “Add filter” to append a row dynamically
    # TODO: verify id
    Click Button    id=add-field-filter

    # Wait until a new row appears
    Wait Until Page Contains Element    xpath=//div[contains(@class,"filter-row")]


Set Field Filter
    [Arguments]    ${index}    ${field}    ${op}    ${value}
    Open Filter Modal

    # If index > existing rows, add new rows
    WHILE    ${index} >=    ${row_count}=Get Element Count    xpath=//div[contains(@class,"filter-row")]
        Add Field Filter Row
    END

    # Select the row
    ${row} =    Get Webelement    xpath=(//div[contains(@class,"filter-row")])[${index + 1}]

    # Select field
    ${field_select} =    Get Webelement    xpath=(//div[contains(@class,"filter-row")])[${index + 1}]//select[1]
    Select From List By Value    ${field_select}    ${field}

    # Select operator
    ${op_select} =    Get Webelement    xpath=(//div[contains(@class,"filter-row")])[${index + 1}]//select[2]
    Select From List By Value    ${op_select}    ${op}

    # Enter value
    Input Text    xpath=(//div[contains(@class,"filter-row")])[${index + 1}]//input    ${value}


Submit Filters
    Open Filter Modal
    Click Button    xpath=//button[@type="submit"]    # TODO confirm
    Sleep    0.5

#### old code #####

Filter By Name
    [Arguments]  ${name}
    Input Text  id=search-bar  ${name}
    Press Key  id=search-bar  ENTER
    Wait Until Page Contains  ${name}


Filter By Type
    [Arguments]  ${type}
    Input Text  id=search-bar  ${type}
    Press Key  id=search-bar  ENTER
    Wait Until Page Contains  ${type}


Filter By Field
    [Arguments]  ${field_type}
    Select From List By Value  id=field-filter-select  ${field_type}
    Click Button  id=apply-filter


Filter By Field Value
    [Arguments]  ${field_type}  ${value}
    Select From List By Value  id=field-select  ${field_type}
    Input Text  id=field-value-input  ${value}
    Click Button  id=apply-filter
    Wait Until Page Contains  ${value}

Sort References
    [Arguments]  ${by}=title  ${order}=asc
    Select From List By Value  id=sort-select  ${by}
    Select From List By Value  id=order-select  ${order}
    Click Button  id=apply-sort
