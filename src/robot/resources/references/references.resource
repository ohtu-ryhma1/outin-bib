*** Settings ***
Documentation    This file provides keywords for interacting with the
...              elements related to references in the website.

Library    SeleniumLibrary

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
