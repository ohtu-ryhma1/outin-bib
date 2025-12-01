*** Settings ***
Documentation     Basic search tests (name and type).

Library           ../libraries/app_library.py

Resource          ../resources/shared/browser.resource
Resource          ../resources/references/verify.resource
Resource          ../resources/references/filter.resource

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Db


*** Variables ***
&{DICT_BOOK_REQUIRED}      author=test_author      title=test_title      year/date=test_year/date
&{DICT_BOOK_REQUIRED_2}    author=test_author_2    title=test_title_2    year/date=test_year/date_2


*** Test Cases ***
Filter By Key Finds Reference
    Create Reference Directly    book    test_key    ${DICT_BOOK_REQUIRED}
    Filter By Key    test_key
    Reference Should Exist    test_key

Filter By Wrong Key Does Not Find Reference
    Create Reference Directly    book    test_key    ${DICT_BOOK_REQUIRED}
    Filter By Key    wrong
    Reference Should Not Exist    test_key

Filter By Type Finds Reference
    Create Reference Directly    book    test_book_1    ${DICT_BOOK_REQUIRED}
    Filter By Types    book
    Reference Should Exist    test_key

Filter By Wrong Type Does Not Find Reference
    Create Reference Directly    book    test_book_1    ${DICT_BOOK_REQUIRED}
    Filter By Types    article
    Reference Should Not Exist    test_key