*** Settings ***
Documentation     Test suite for Searching references.

Library           ../libraries/app_library.py

Resource          ../resources/shared/browser.resource
Resource          ../resources/actions/search.resource
Resource          ../resources/actions/validate.resource

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Db And Go To Homepage


*** Variables ***
&{FIELDS_1}    author=test_author      title=test_title      year/date=test_year/date
&{FIELDS_2}    author=test_author_2    title=test_title_2    year/date=test_year/date_2

@{TYPES_1}      book
@{TYPES_2}      article
&{FILTERS_1}    author=test_author
&{FILTERS_2}    author=wrong_author



*** Test Cases ***
Search By Key Finds Reference
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Go To Homepage
    Search References    key=test_key
    Reference Card Should Be Visible    test_key

Search By Wrong Key Does Not Find Reference
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Go To Homepage
    Search References    key=wrong_key
    Reference Card Should Not Be Visible    test_key

Search By Type Finds Reference
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Go To Homepage
    Search References    types=${TYPES_1}
    Reference Card Should Be Visible    test_key

Search By Wrong Type Does Not Find Reference
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Go To Homepage
    Search References    types=${TYPES_2}
    Reference Card Should Not Be Visible    test_key

Search By Field Finds Reference
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Go To Homepage
    Search References    filters=${FILTERS_1}
    Reference Card Should Be Visible    test_key

Search By Wrong Field Does Not Find Reference
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Go To Homepage
    Search References    filters=${FILTERS_2}
    Reference Card Should Not Be Visible    test_key

Search By Field Value Finds Multiple References
    Create Reference Via Request    book    test_key      ${FIELDS_1}
    Create Reference Via Request    book    test_key_2    ${FIELDS_2}
    Go To Homepage
    Search References    filters=${FILTERS_1}
    Reference Card Should Be Visible    test_key
    Reference Card Should Be Visible    test_key_2


*** Keywords ***
Reset Db And Go To Homepage
    Reset Db
    Go To Homepage
