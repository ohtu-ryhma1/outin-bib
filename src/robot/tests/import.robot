*** Settings ***
Documentation    Test suite for importing references.

Library           OperatingSystem
Library           ../libraries/repository_api.py

Resource          ../resources/shared/browser.resource
Resource          ../resources/actions/import.resource
Resource          ../resources/actions/validate.resource
Resource          ../resources/components/flash.resource

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Db And Go To Import Page


*** Variables ***
${URL_IMPORT}          import-export
${VALID_IMPORT}        ${CURDIR}/../data/valid_import.bib
${INVALID_IMPORT}      ${CURDIR}/../data/invalid_import.bib
${CROSSREF_PARENT}     ${CURDIR}/../data/crossref_parent.bib
${CROSSREF_CHILD}      ${CURDIR}/../data/crossref_child.bib


*** Test Cases ***
Import Reference From Text Succeeds
    ${bibtex} =    Get File    ${VALID_IMPORT}
    Import From Text    ${bibtex}
    Wait Until Page Is Open    ${URL_IMPORT}
    Wait Until Flash Message Is Visible
    Go To Homepage
    Reference Card Should Be Visible    test_reference

Import Duplicate Reference From Text Shows Error
    ${bibtex} =    Get File    ${VALID_IMPORT}
    Import From Text    ${bibtex}
    Wait Until Page Is Open    ${URL_IMPORT}
    Wait Until Flash Message Is Visible
    Import From Text    ${bibtex}
    Wait Until Page Is Open    ${URL_IMPORT}
    Wait Until Flash Message Is Visible
    Go To Homepage
    Reference Card Should Be Visible    test_reference

Import Crossref Parent Succeeds
    ${bibtex} =    Get File    ${CROSSREF_PARENT}
    Import From Text    ${bibtex}
    Wait Until Page Is Open    ${URL_IMPORT}
    Wait Until Flash Message Is Visible
    Go To Homepage
    Reference Card Should Be Visible    parent_book

Import Crossref Parent Then Child Succeeds
    ${parent_bibtex} =    Get File    ${CROSSREF_PARENT}
    Import From Text    ${parent_bibtex}
    Wait Until Page Is Open    ${URL_IMPORT}
    Wait Until Flash Message Is Visible
    Go To Homepage
    Reference Card Should Be Visible    parent_book

    Go To Page    ${URL_IMPORT}
    ${child_bibtex} =    Get File    ${CROSSREF_CHILD}
    Import From Text    ${child_bibtex}
    Wait Until Page Is Open    ${URL_IMPORT}
    Wait Until Flash Message Is Visible
    Go To Homepage
    Reference Card Should Be Visible    glashow_partial

Import Reference From File Succeeds
    ${path} =    Normalize Path    ${VALID_IMPORT}
    Import From File    ${path}
    Wait Until Page Is Open    ${URL_IMPORT}
    Wait Until Flash Message Is Visible
    Go To Homepage
    Reference Card Should Be Visible    test_reference

Import Reference From Invalid File Shows Error
    ${path} =    Normalize Path    ${INVALID_IMPORT}
    Import From File    ${path}
    Wait Until Page Is Open    ${URL_IMPORT}
    Wait Until Flash Message Contains    Parse error
    Go To Homepage
    Reference Card Should Not Be Visible    invalid_reference

*** Keywords ***
Reset Db And Go To Import Page
    Reset Db
    Go To Page    ${URL_IMPORT}
