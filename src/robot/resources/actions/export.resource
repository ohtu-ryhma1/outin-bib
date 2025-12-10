*** Settings ***
Documentation     High-level keywords for exporting data using the export component.

Resource          ../components/export.resource


*** Keywords ***
Export To Text
    [Documentation]    Return the exported text.
    ${exported_text} =    Copy Exported Text
    RETURN    ${exported_text}

Export File
    [Documentation]    Download the exported file.
    Export File
