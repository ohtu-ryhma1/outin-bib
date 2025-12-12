*** Settings ***
Documentation    Intermediate level keywords for interacting with the search component.

Resource    ../shared/ui.resource


*** Variables ***
${BUTTON_SEARCH_OPEN}          id:open-search-button
${INPUT_REF_KEY}               id:ref-key
${SELECT_REF_TYPE}             css:div.choices>div.choices__inner
${BUTTON_FILTER_ADD}           id:add-filter-button
${BUTTON_SUBMIT}               id:submit-search-button
${SELECT_FIELD_FILTER_LAST}    css:div.field-filter:last-of-type select
${INPUT_FIELD_FILTER_LAST}     css:div.field-filter:last-of-type input


*** Keywords ***
Open Search Window
    [Documentation]    Open the search window by clicking the search button.
    UI Click Element    ${BUTTON_SEARCH_OPEN}

Input Search Key
    [Documentation]    Input a given `ref_key` into the reference key input.
    [Arguments]    ${ref_key}
    UI Input Text    ${INPUT_REF_KEY}    ${ref_key}

Open Reference Type Dropdown
    [Documentation]    Open the reference type dropdown.
    UI Click Element    ${SELECT_REF_TYPE}

Add Reference Type
    [Documentation]    Select a given `type` from the dropdown.
    [Arguments]    ${type}
    UI Click Element    xpath://div[contains(@class,'choices__list--dropdown')]//div[contains(@class,'choices__item') and text()='${type}']

Close Reference Type Dropdown
    [Documentation]    Close the reference type dropdown.
    UI Press Key    ESCAPE

Add Field Filter
    [Documentation]    Add a new field filter.
    UI Click Element    ${BUTTON_FILTER_ADD}

Set Field Filter
    [Documentation]    Set the `value` of the last added field filter for the given `field`.
    [Arguments]    ${field}    ${value}
    UI Select Option    ${SELECT_FIELD_FILTER_LAST}    ${field}
    UI Input Text    ${INPUT_FIELD_FILTER_LAST}    ${value}

Submit Search
    [Documentation]    Submit the search form.
    UI Click Element    ${BUTTON_SUBMIT}
