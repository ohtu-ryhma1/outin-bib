*** Settings ***
Documentation     Intermediate level keywords for interacting with the export component.

Resource    ../shared/ui.resource


*** Variables ***
${BUTTON_COPY_EXPORT}        id:copy-export-button
${BUTTON_DOWNLOAD_EXPORT}    id:download-export-button


*** Keywords ***
Copy Exported Text
    [Documentation]    Copy the exported text to clipboard.
    UI Click Element    ${BUTTON_COPY_EXPORT}

Export File
    [Documentation]    Download the exported file.
    UI Click Element    ${BUTTON_DOWNLOAD_EXPORT}
