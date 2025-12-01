*** Settings ***
Documentation    This file provides keywords for interacting with the
...              import/export page elements.

Library    SeleniumLibrary

Resource    ../shared/browser.resource


*** Variables ***
${IMPORT_EXPORT_URL}    http://localhost:5001/import-export

${BIBTEX_TEXTAREA}      id:bibtex-text
${BIBTEX_FILE_INPUT}    id:bibtex-file


*** Keywords ***
Go To Import Export Page
    Go To    ${IMPORT_EXPORT_URL}

Import Export Page Should Be Open
    Location Should Contain    /import-export

Input Bibtex Text
    [Arguments]    ${text}
    Input Text    ${BIBTEX_TEXTAREA}    ${text}

Click Export All Button
    Click Button    xpath://button[contains(., 'Export All')]

Click Import From Text Button
    Click Button    xpath://button[contains(., 'Import from Text')]

Click Import From File Button
    Click Button    xpath://button[contains(., 'Import from File')]
