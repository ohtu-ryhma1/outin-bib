*** Settings ***
Documentation     Test suite for editing references.

Library           ../libraries/repository_api.py

Resource          ../resources/shared/browser.resource
Resource          ../resources/actions/edit.resource
Resource          ../resources/actions/validate.resource

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Db And Go To Homepage


*** Variables ***
${URL_EDIT_REFERENCE}    edit-reference

&{FIELDS_1}             author=test_author          title=test_title      year/date=test_year/date
&{FIELDS_2}             author=test_author_2        title=test_title_2    year/date=test_year/date_2
&{FIELDS_3}             author=
&{FIELDS_OPTIONAL_1}    language=test_language      part=test_part        pages=test_pages
&{FIELDS_OPTIONAL_2}    language=test_language_2    part=test_part_2      pages=test_pages_2


*** Test Cases ***
Editing Key Succeeds
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Go To Homepage
    Click Reference Card    test_key
    Edit Reference    test_key    new_ref_key=test_key_2
    Wait Until Page Is Homepage
    Reference Card Should Have Correct Data    test_key_2    book    ${FIELDS_1}

Editing Required Fields Succeeds
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Go To Homepage
    Click Reference Card    test_key
    Edit Reference    test_key    new_fields=${FIELDS_2}
    Wait Until Page Is Homepage
    Reference Card Should Have Correct Data    test_key    book    ${FIELDS_2}

Adding Optional Fields Succeeds
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Go To Homepage
    Click Reference Card    test_key
    Edit Reference    test_key    new_fields=${FIELDS_OPTIONAL_1}
    Wait Until Page Is Homepage
    Reference Card Should Have Correct Data    test_key    book    ${FIELDS_1}
    Click Reference Card    test_key
    Reference Form Should Have Correct Data    test_key    book    ${FIELDS_OPTIONAL_1}

Editing Optional Fields Succeeds
    Skip
    ${fields_combined} =    Evaluate    {**${FIELDS_1}, **${FIELDS_OPTIONAL_1}}
    Create Reference Via Request    book    test_key    ${fields_combined}
    Go To Homepage
    Click Reference Card    test_key
    Edit Reference    test_key    new_fields=${FIELDS_OPTIONAL_2}
    Wait Until Page Is Homepage
    Reference Card Should Have Correct Data    test_key    book    ${FIELDS_1}
    Click Reference Card    test_key
    Reference Form Should Have Correct Data    test_key    book    ${FIELDS_OPTIONAL_2}

Removing Required Field Fails
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Go To Homepage
    Click Reference Card    test_key
    Edit Reference    test_key    new_fields=${FIELDS_3}
    Wait Until Page Is Open    ${URL_EDIT_REFERENCE}
    Go To Homepage
    Reference Card Should Have Correct Data    test_key    book    ${FIELDS_1}


*** Keywords ***
Reset Db And Go To Homepage
    Reset Db
    Go To Homepage
