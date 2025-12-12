*** Settings ***
Documentation     High-level keywords for exporting data using the export component.

Library          ../../libraries/clipboard_api.py

Resource          ../components/export.resource


*** Keywords ***
Get Exported Text From Page
    [Documentation]    Get the exported text directly.
    ${exported_text} =    Get Exported Text
    RETURN    ${exported_text}

Get Exported Text From Clipboard
    [Documentation]    Use the copy to clipboard feature and return the clipboard contents.
    Copy Export Text To Clipboard
    Sleep    0.1s
    ${clipboard} =    Clipboard Get
    RETURN    ${clipboard}

Export File
    [Documentation]    Download the exported file.
    Download Export File
