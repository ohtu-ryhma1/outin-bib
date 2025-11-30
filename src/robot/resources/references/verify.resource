*** Settings ***
Documentation    This file provides keywords to verify that certain references exist

Resource    references.resource

*** Keywords ***
Reference Should Exist
    [Arguments]    ${ref_key}
    Go To Homepage
    Element Should Be Visible    xpath://p[@class='ref-key' and text()='${ref_key}']

Reference Should Not Exist
    [Arguments]   ${ref_key}
    Go To Homepage
    Element Should Not Be Visible   xpath://p[@class='ref-key' and text()='${ref_key}']

Reference Card Should Display Correct Info
    [Arguments]    ${ref_key}    ${ref_type}    ${required_fields}
    Go To Homepage
    ${ref} =    Get Reference Card    ${ref_key}
    Element Should Contain    ${ref}    ${ref_type}

    FOR    ${field_type}    ${field_value}    IN    &{required_fields}
        Element Should Contain    ${ref}    ${field_type}
        Element Should Contain    ${ref}    ${field_value}
    END

Reference Should Have Correct Fields
    [Arguments]    ${ref_key}    ${ref_type}    ${fields}
    Go To Edit Page    ${ref_key}

    FOR    ${field_type}    ${field_value}    IN    &{fields}
        Element Should Contain    id:${field_type}    ${field_value}
    END