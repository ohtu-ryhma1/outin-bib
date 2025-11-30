*** Settings ***
Library           ../libraries/app_library.py

Resource          ../resources/shared/browser.resource
Resource          ../resources/references/edit.resource
Resource          ../resources/references/verify.resource

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Db


*** Variables ***
&{DICT_BOOK_REQUIRED}      author=test_author      title=test_title      year/date=test_year/date
&{DICT_BOOK_REQUIRED_2}    author=test_author_2    title=test_title_2    year/date=test_year/date_2
&{DICT_BOOK_REQUIRED_3}    author=                 title=test_title_2    year/date=test_year/date_2

&{DICT_BOOK_OPTIONAL}      language=test_language      part=test_part      pages=test_pages
&{DICT_BOOK_OPTIONAL_2}    language=test_language_2    part=test_part_2    pages=test_pages_2


*** Test Cases ***
Editing Reference Key Succeeds
    Create Reference Directly    book    test_key    ${DICT_BOOK_REQUIRED}
    Edit Reference    test_key    test_key    ${DICT_BOOK_REQUIRED_2}
    Homepage Should Be Open
    Reference Card Should Display Correct Info    test_key    book    ${DICT_BOOK_REQUIRED_2}

Editing Reference Required Fields Succeeds
    Create Reference Directly    book    test_key    ${DICT_BOOK_REQUIRED}
    Edit Reference    test_key    test_key    ${DICT_BOOK_REQUIRED_2}
    Homepage Should Be Open
    Reference Card Should Display Correct Info    test_key    book    ${DICT_BOOK_REQUIRED_2}

Editing Reference Required And Optional Fields Succeeds
    ${dict_book_combined} =      Evaluate    {**${DICT_BOOK_REQUIRED}, **${DICT_BOOK_OPTIONAL}}
    ${dict_book_combined_2} =    Evaluate    {**${DICT_BOOK_REQUIRED_2}, **${DICT_BOOK_OPTIONAL_2}}
    Create Reference Directly    book    test_key    ${dict_book_combined}
    Edit Reference    test_key    test_key    ${DICT_BOOK_OPTIONAL_2}
    Homepage Should Be Open
    Reference Card Should Display Correct Info    test_key    book    ${DICT_BOOK_REQUIRED_2}
    Reference Should Have Correct Fields    test_key    book    ${dict_book_combined_2}

Editing Reference Removing Required Field Fails
    Create Reference Directly    book    test_key    ${DICT_BOOK_REQUIRED}
    Edit Reference    test_key    test_key    ${DICT_BOOK_REQUIRED_3}
    Edit Page Should Be Open
    Reference Card Should Display Correct Info    test_key    book    ${DICT_BOOK_REQUIRED}