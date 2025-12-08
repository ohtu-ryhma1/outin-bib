*** Settings ***
Library            OperatingSystem
Library           ../libraries/app_library.py

Resource          ../resources/shared/browser.resource
Resource          ../resources/references/import_export.resource
Resource          ../resources/references/references.resource
Resource          ../resources/references/verify.resource

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Db


*** Test Cases ***
Import Export Page Is Accessible
    Go To Import Export Page
    Import Export Page Should Be Open

Import Reference From Text Succeeds
    Go To Import Export Page
    Input Bibtex Text    ${VALID_BIBTEX}
    Click Import From Text Button
    Import Export Page Should Be Open
    Go To Homepage
    Reference Should Exist    imported_article

Import Duplicate Reference Shows Error
    Go To Import Export Page
    Input Bibtex Text    ${VALID_BIBTEX}
    Click Import From Text Button
    Go To Import Export Page
    Input Bibtex Text    ${VALID_BIBTEX}
    Click Import From Text Button
    Page Should Contain    Reference with this key already exists

Import Crossref Parent Succeeds
    Go To Import Export Page
    Input Bibtex Text    ${CROSSREF_PARENT}
    Click Import From Text Button
    Go To Homepage
    Reference Should Exist    parent_book

Import Crossref Parent Then Child Succeeds
    Go To Import Export Page
    Input Bibtex Text    ${CROSSREF_PARENT}
    Click Import From Text Button
    Go To Homepage
    Reference Should Exist    parent_book

    Go To Import Export Page
    Input Bibtex Text    ${CROSSREF_CHILD}
    Click Import From Text Button
    Go To Homepage
    Reference Should Exist    glashow_partial

Import Reference From File Succeeds
    Go To Import Export Page
    ${path}=    Normalize Path    ${CURDIR}/../resources/test_files/valid_import.bib
    Choose File    id:import-file-input    ${path}
    Click Import From File Button
    Go To Homepage
    Reference Should Exist    file_imported_ref

Import Reference From Invalid File Shows Error
    Go To Import Export Page
    ${path}=    Normalize Path    ${CURDIR}/../resources/test_files/invalid_import.bib
    Choose File    id:import-file-input    ${path}
    Click Import From File Button
    Page Should Contain    Parse error
