*** Settings ***
Documentation    Keywords for using the search/filter modal on the homepage.
...              Provides tools for searching by key, type, and field/value filters.

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
    Click Element    xpath=//div[@id="ref-type-filter"]//div[contains(@class,"choices")]
    Wait Until Element Is Visible
    ...    xpath=//div[contains(@class,"choices__list--dropdown")]//div[contains(@class,"choices__item")]
    ...    timeout=5s
    FOR    ${type}    IN    @{types}
        Click Element    xpath=//div[contains(@class,"choices__item") and normalize-space(text())="${type}"]
    END
    Execute JavaScript    document.querySelector('#ref-type').closest('.choices').classList.remove('is-open');
    Sleep    0.5s
    Submit Search

Add Field Filter
    [Documentation]    Click “+” (Add filter) button to append a new field-filter row.
    Click Button    id=add-field-filter
    Wait Until Page Contains Element
    ...    xpath=//div[contains(@class,"field-filter")]

Set Field Filter
    [Documentation]    Select a field and input a value in the last field-filter row.
    [Arguments]    ${field}    ${value}
    Wait Until Page Contains Element
    ...    xpath=//div[contains(@class,"field-filter")]
    ${row}=    Get Webelement
    ...    xpath=(//div[contains(@class,"field-filter")])[last()]
    ${field_select}=    Get Webelement
    ...    xpath=(//div[contains(@class,"field-filter")])[last()]//select
    Select From List By Label    ${field_select}    ${field}
    Input Text
    ...    xpath=(//div[contains(@class,"field-filter")])[last()]//input
    ...    ${value}

