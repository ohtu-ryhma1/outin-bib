*** Settings ***
Documentation     Basic search tests (name and type).
Resource          ../resources/shared/browser.resource
Resource          ../resources/references/verify.resource
Resource          ../resources/search/filter.resource
Library           ../libraries/app_library.py

Suite Setup       Open And Configure Browser
Test Setup        Reset Db
Suite Teardown    Close Browser

*** Variables ***
&{BOOK_FIELDS}    author=John    title=TestTitle    year/date=2024

*** Test Cases ***
Search By Name Shows Matching Reference
    Create Reference Directly    book    RefA    ${BOOK_FIELDS}
    Filter By Name    TestTitle
    Reference Should Exist    RefA

Search By Type Shows Matching Reference
    Create Reference Directly    book    RefB    ${BOOK_FIELDS}
    Select Types    book
    Submit Filters
    Reference Should Exist    RefB
