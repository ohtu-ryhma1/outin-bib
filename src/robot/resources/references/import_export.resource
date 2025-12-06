*** Settings ***
Documentation    This file provides keywords for interacting with the
...              import/export page elements.

Resource    import_export_ui.resource


*** Keywords ***
Go To Import Export
    Go To    ${IMPORT_EXPORT_URL}

Import Export Should Be Open
    Import Export Page Should Be Open

Import From Text
    [Arguments]    ${bibtex_text}
    Go To Import Export Page
    Input Bibtex Text    ${bibtex_text}
    Click Import From Text Button

Import From File
    [Arguments]    ${file_path}
    Go To Import Export Page
    Choose File    ${BIBTEX_FILE_INPUT}    ${file_path}
    Click Import From File Button

Export All
    Go To Import Export Page
    Click Export All Button
