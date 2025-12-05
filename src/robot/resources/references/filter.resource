*** Settings ***
Documentation    Keywords for using the search/filter modal on the homepage.
...              Existing filters are rendered in the template, and new ones can be
...              added dynamically with the “Add filter” button.

Library          SeleniumLibrary
Resource         references.resource


*** Keywords ***
Filter By Key
    [Arguments]    ${key}
    Go To Homepage
    Open Search Window
    Input Search Key    ${key}
    Submit Search

Filter By Types
    [Arguments]    @{types}
    Go To Homepage
    Open Search Window

    FOR    ${type}    IN    @{types}
        Select Search Type    ${type}
    END

    Submit Search

Add Field Filter
    # Click “Add filter” to append a row dynamically
    # TODO: verify id
    Click Button    id=add-filter-button

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

