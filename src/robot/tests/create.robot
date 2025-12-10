*** Settings ***
Documentation     Test suite for creating references.

Library           ../libraries/repository_api.py

Resource          ../resources/shared/browser.resource
Resource          ../resources/actions/create.resource
Resource          ../resources/actions/validate.resource

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Db And Go To New Reference Page


*** Variables ***
${URL_NEW_REFERENCE}    new-reference
&{FIELDS}    author=test_author    title=test_title    year/date=test_year/date


*** Test Cases ***
Creating A Reference Succeeds
    Create Reference    ref_type=book    ref_key=test_key    fields=${FIELDS}
    Wait Until Page Is Homepage
    Reference Card Should Have Correct Data    test_key    ref_type=book    fields=${FIELDS}

Creating A Reference Without Key Fails
    Create Reference    ref_type=book    fields=${FIELDS}
    Wait Until Page Is Open    ${URL_NEW_REFERENCE}
    Go To Homepage
    Reference Card Should Not Be Visible    test_key

Creating A Reference Without Required Fields Fails
    Create Reference    ref_type=book    ref_key=test_key
    Wait Until Page Is Open    ${URL_NEW_REFERENCE}
    Go To Homepage
    Reference Card Should Not Be Visible    test_key


*** Keywords ***
Reset Db And Go To New Reference Page
    Reset Db
    Go To Page    ${URL_NEW_REFERENCE}
