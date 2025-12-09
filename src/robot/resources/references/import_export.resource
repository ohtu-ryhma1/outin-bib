*** Settings ***
Documentation    This file provides keywords for interacting with the
...              import/export page elements.

Library     OperatingSystem
Resource    import_export_ui.resource

*** Variables ***
${VALID_BIBTEX}       @article{imported_article,\n  author = "Test Author",\n  title = "Imported Article Title",\n  journaltitle = "Test Journal",\n  year = 2024,\n}
${CROSSREF_PARENT}    @book{parent_book,\n  author = {Glashow, Sheldon},\n  title = {Collected Works of S. Glashow},\n  publisher = {Oxford University Press},\n  date = {1965},\n}
${CROSSREF_CHILD}     @inbook{glashow_partial,\n  author = {Glashow, Sheldon},\n  title = {Partial Symmetries of Weak Interactions},\n  crossref = {parent_book},\n  pages = {579--588},\n}
&{DICT_BOOK}       author=test_author    title=test_title    year/date=test_year/date
&{DICT_ARTICLE}    author=testAuthor     title=testTitle     journaltitle=journalTitle    year/date=test_year_article
${FILE_NAME}       references.bib

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

#Accept Handle Alert
# AUTOMATISOI TOI HANDLE ALERTIN ACCEPTAUS

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
