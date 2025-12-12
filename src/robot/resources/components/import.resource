*** Settings ***
Documentation     Intermediate level keywords for interacting with the import window.

Resource    ../shared/ui.resource


*** Variables ***
${TEXTAREA_IMPORT}      id:import-textarea
${FILE_IMPORT}          id:import-file-input
${BUTTON_IMPORT_TEXT}   id:import-text-button
${BUTTON_IMPORT_FILE}   id:import-file-button


*** Keywords ***
Input Import Text
    [Documentation]    Input the given `text` into the import textarea.
    [Arguments]    ${text}
    UI Input Text    ${TEXTAREA_IMPORT}    ${text}

Submit Import From Text
    [Documentation]    Submit the text import form.
    UI Click Element    ${BUTTON_IMPORT_TEXT}

Upload Import File
    [Documentation]    Upload a file from the given `file_path`.
    [Arguments]    ${file_path}
    UI Choose File    ${FILE_IMPORT}    ${file_path}

Submit Import From File
    [Documentation]    Submit the file import form.
    UI Click Element    ${BUTTON_IMPORT_FILE}
