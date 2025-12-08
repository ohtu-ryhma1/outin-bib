*** Settings ***
Library            OperatingSystem
Library            ../libraries/app_library.py

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

Export Empty Reference To Copy Succeeds
    Go To Import Export Page
    Click Export Copy Button
    Handle Alert  ACCEPT
    ${export_text}=  Get Value  ${EXPORT_TEXTAREA}
    Should Contain  ${export_text}  ""

Export Single Reference To Copy Succeeds
    Go To Import Export Page
    Import From Text  ${VALID_BIBTEX}
    Go To Import Export Page
    Click Export Copy Button
    Handle Alert  ACCEPT
    ${export_text}=  Get Value  ${EXPORT_TEXTAREA}
    Should Contain  ${export_text}  imported_article

Export Crossref Parent And Child To Copy Succeeds
    Import From Text  ${CROSSREF_PARENT}
    Import From Text  ${CROSSREF_CHILD}
    Go To Import Export Page
    Click Export Copy Button
    Handle Alert  ACCEPT
    ${export_text}=  Get Value  ${EXPORT_TEXTAREA}
    Should Contain  ${export_text}  parent_book
    Should Contain  ${export_text}  glashow_partial
