*** Settings ***
Documentation    This file provides keywords for interacting with the
...              import/export page elements.

Library     OperatingSystem
Resource    import_export_ui.resource

*** Variables ***
${OUTPUT_DIR}        ${CURDIR}/../downloads
${EXPORT_FILE}       references.bib
${EXPORT_FILE_PATH}  ${OUTPUT_DIR}/${EXPORT_FILE}
${VALID_BIBTEX}       @article{imported_article,\n  author = "Test Author",\n  title = "Imported Article Title",\n  journaltitle = "Test Journal",\n  year = 2024,\n}
${CROSSREF_PARENT}    @book{parent_book,\n  author = {Glashow, Sheldon},\n  title = {Collected Works of S. Glashow},\n  publisher = {Oxford University Press},\n  date = {1965},\n}
${CROSSREF_CHILD}     @inbook{glashow_partial,\n  author = {Glashow, Sheldon},\n  title = {Partial Symmetries of Weak Interactions},\n  crossref = {parent_book},\n  pages = {579--588},\n}

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

Export Text Should Contain
    [Arguments]  ${expected}
    ${text}=  Get Value  ${EXPORT_TEXTAREA}
    Should Contain  ${text}  ${expected}

Export File
    [Documentation]  Click Export as file and wait until file exists
    Go To Import Export Page
    Click Element  ${EXPORT_FILE_BUTTON}
    Wait Until Keyword Succeeds  10x  1s  File Should Exist  ${EXPORT_FILE_PATH}

Exported File Should Exist
    File Should Exist  ${EXPORT_FILE_PATH}

Exported File Should Contain
    [Arguments]  ${text}
    ${content}=  Get File  ${EXPORT_FILE_PATH}
    Should Contain  ${content}  ${text}
