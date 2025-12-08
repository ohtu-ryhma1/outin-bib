*** Settings ***
Documentation    Low-level UI keywords and selectors for the Import/Export page.

Library    SeleniumLibrary

Resource    ../shared/browser.resource


*** Variables ***
${IMPORT_EXPORT_URL}    http://localhost:5001/import-export
${BIBTEX_TEXTAREA}      id:import-textarea
${BIBTEX_FILE_INPUT}    id:import-file-input
${BUTTON_EXPORT_ALL}    xpath=//button[contains(., 'Export All')]
${BUTTON_IMPORT_TEXT}   xpath://button[contains(., 'Import from Text')]
${BUTTON_IMPORT_FILE}   xpath://button[contains(., 'Import from File')]
${EXPORT_FILE_BUTTON}   xpath=//form[@action="/export/file"]//button
${EXPORT_COPY_BUTTON}   id:copy-export-button
${EXPORT_TEXTAREA}      id:export-textarea

*** Keywords ***
Go To Import Export Page
    Go To    ${IMPORT_EXPORT_URL}

Import Export Page Should Be Open
    Location Should Contain    /import-export

Input Bibtex Text
    [Arguments]    ${text}
    Wait For Element Visible    ${BIBTEX_TEXTAREA}
    Input Text    ${BIBTEX_TEXTAREA}    ${text}

Click Export All Button
    Click Button    ${BUTTON_EXPORT_ALL}

Click Import From Text Button
    Click Button    ${BUTTON_IMPORT_TEXT}

Click Import From File Button
    Click Button    ${BUTTON_IMPORT_FILE}

Click Export Copy Button
    Click Button  ${EXPORT_COPY_BUTTON}

Click Export File Button
    Click Button  ${EXPORT_FILE_BUTTON}
