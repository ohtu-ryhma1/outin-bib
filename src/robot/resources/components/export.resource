*** Settings ***
Documentation     Intermediate level keywords for interacting with the export component.

Resource    ../shared/ui.resource
Library     ../../libraries/clipboard_api.py


*** Variables ***
${TEXTAREA_EXPORT}           id:export-textarea
${BUTTON_COPY_EXPORT}        id:copy-export-button
${BUTTON_DOWNLOAD_EXPORT}    id:download-export-button


*** Keywords ***
Get Exported Text
    [Documentation]    Get the exported text directly.
    ${exported_text} =    UI Get Text    ${TEXTAREA_EXPORT}
    RETURN    ${exported_text}

Copy Export Text To Clipboard
    [Documentation]    Click the button to copy exported text to clipboard.
    UI Click Element    ${BUTTON_COPY_EXPORT}

Download Export File
    [Documentation]    Download the exported file.
    UI Click Element    ${BUTTON_DOWNLOAD_EXPORT}
