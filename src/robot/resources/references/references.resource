*** Settings ***
Documentation    This file provides keywords for interacting with the
...              elements related to references in the website.

Library    SeleniumLibrary

Resource   ../shared/browser.resource

*** Variables ***
${HOME_URL}             http://localhost:5001
${NEW_REFERENCE_URL}    new-reference
${EDIT_REFERENCE_URL}   edit-reference

# locators
${SELECT_REF_TYPE}            id:ref-type-input
${INPUT_REF_KEY}              id:ref-key-input
${SELECT_FIELD_TYPE}          id:field-select
${BUTTON_ADD_FIELD}           id:field-select
${BUTTON_SUBMIT}              id:submit
${BUTTON_SEARCH_OPEN}         id:open-search-button
${INPUT_SEARCH_KEY}           id:ref-key
${SELECT_FILTER_REF_TYPE}     id:ref-type
${BUTTON_FILTER_ADD}          id:add-filter-button
${BUTTON_SEARCH_SUBMIT}       id:submit-search-button
${REF_TYPE_DROPDOWN}          xpath=//div[@id="ref-type-filter"]//div[contains(@class,"choices")]
${REF_TYPE_DROPDOWN_LIST}     xpath=//div[contains(@class,"choices__list--dropdown")]//div[contains(@class,"choices__item")]
${FIELD_FILTER_LAST_SELECT}   xpath=(//div[contains(@class,"field-filter")])[last()]//select
${FIELD_FILTER_LAST_INPUT}    xpath=(//div[contains(@class,"field-filter")])[last()]//input


*** Keywords ***
Homepage Should Be Open
    Location Should Contain    ${HOME_URL}

Create Page Should Be Open
    Location Should Contain    ${HOME_URL}/${NEW_REFERENCE_URL}

Edit Page Should Be Open
    Location Should Contain    ${HOME_URL}/${EDIT_REFERENCE_URL}

Go To Homepage
    Go To    ${HOME_URL}

Go To Create Page
    Go To    ${HOME_URL}/${NEW_REFERENCE_URL}

Go To Edit Page
    [Arguments]    ${ref_key}
    Go To Homepage
    Click Element    xpath://a[@class = 'ref-card' and .//p[text()='${ref_key}']]

Get Reference Card
    [Arguments]    ${ref_key}
    ${ref_card} =    Get Webelement   xpath://a[@class = 'ref-card' and .//p[text()='${ref_key}']]
    RETURN    ${ref_card}

Select Reference Type
    [Arguments]    ${ref_type}
    Select From List By Label    ${SELECT_REF_TYPE}    ${ref_type}

Input Reference Key
    [Arguments]    ${ref_key}
    Input Text    ${INPUT_REF_KEY}    ${ref_key}

Input Field
    [Arguments]    ${field_type}    ${field_value}
    Input Text    id:${field_type}    ${field_value}

Add Field
    [Arguments]    ${field_type}
    Select From List By Value    ${SELECT_FIELD_TYPE}    ${field_type}
    Click Button    ${BUTTON_ADD_FIELD}

Does Field Exist
    [Arguments]    ${field_type}
    ${field_exists} =    Run Keyword And Return Status    Element Should Be Visible    id:${field_type}
    RETURN    ${field_exists}

Submit Reference Form
    Scroll Element Into View    ${BUTTON_SUBMIT}
    Click Button    ${BUTTON_SUBMIT}

Open Search Window
    Click Element    ${BUTTON_SEARCH_OPEN}

Input Search Key
    [Arguments]    ${search_key}
    Input Text    ${INPUT_SEARCH_KEY}    ${search_key}

Select Search Type
    [Arguments]    ${search_type}
    Select From List By Label    ${SELECT_FILTER_REF_TYPE}    ${search_type}

Add Search Field Filter
    Click Button    ${BUTTON_FILTER_ADD}

Submit Search
    Click Button    ${BUTTON_SEARCH_SUBMIT}

Open Reference Type Dropdown
    Click Element    ${REF_TYPE_DROPDOWN}
    Wait For Element Visible    ${REF_TYPE_DROPDOWN_LIST}
    Sleep    0.5s

Select Reference Type Option
    [Arguments]    ${type}
    Wait For Element Visible    xpath=//div[contains(@class,"choices__item") and normalize-space(text())="${type}"]
    Wait Until Keyword Succeeds    3x    1s    Click Element    xpath=//div[contains(@class,"choices__item") and normalize-space(text())="${type}"]

Close Reference Type Dropdown
    Execute JavaScript    document.querySelector('#ref-type').closest('.choices').classList.remove('is-open');

Add Field Filter
    Click Button    ${BUTTON_FILTER_ADD}
    Wait For Element Visible    xpath=//div[contains(@class,"field-filter")]

Set Field Filter
    [Arguments]    ${field}    ${value}
    Wait For Element Visible    xpath=//div[contains(@class,"field-filter")]
    Select From List By Label    ${FIELD_FILTER_LAST_SELECT}    ${field}
    Input Text    ${FIELD_FILTER_LAST_INPUT}    ${value}
