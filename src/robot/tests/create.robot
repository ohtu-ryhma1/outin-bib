*** Settings ***
Library           ../libraries/app_library.py

Resource          ../resources/shared/browser.resource
Resource          ../resources/references/create.resource
Resource          ../resources/references/verify.resource

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Db


*** Variables ***
&{DICT_BOOK_REQUIRED}    author=test_author    title=test_title    year/date=test_year/date

*** Test Cases ***
Creating A Reference Succeeds
    Create A Reference    book    test_key    ${DICT_BOOK_REQUIRED}
    Homepage Should Be Open
    Reference Should Exist    test_key
    Reference Card Should Display Correct Info    test_key    book    ${DICT_BOOK_REQUIRED}

Creating A Reference Without Key Fails
    Create A Reference Without Key    book    ${DICT_BOOK_REQUIRED}
    Create Page Should Be Open

Creating A Reference Without Required Fields Fails
    Create A Reference Without Required Fields    book    test_key
    Create Page Should Be Open