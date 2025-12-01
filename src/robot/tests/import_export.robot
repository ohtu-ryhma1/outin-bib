*** Settings ***
Library           ../libraries/app_library.py

Resource          ../resources/shared/browser.resource
Resource          ../resources/references/import_export.resource
Resource          ../resources/references/references.resource
Resource          ../resources/references/verify.resource

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Db


*** Variables ***
${VALID_BIBTEX}    @article{imported_article,\n  author = "Test Author",\n  title = "Imported Article Title",\n  journaltitle = "Test Journal",\n  year = 2024,\n}


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
