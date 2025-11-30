*** Settings ***
Documentation    This file provides keywords to create references
...              with different configurations

Resource    references.resource


*** Variables ***
&{EMPTY_DICT}


*** Keywords ***
Create A Reference
    [Arguments]    ${ref_type}    ${ref_key}    ${required_fields}    ${optional_fields}=${EMPTY_DICT}
    Go To Create Page
    Select Reference Type    ${ref_type}
    Input Reference Key    ${ref_key}

    FOR    ${field_type}    ${field_value}    IN    &{required_fields}
        Input Field    ${field_type}    ${field_value}
    END

    FOR    ${field_type}    ${field_value}    IN    &{optional_fields}
        Add Field    ${field_type}
        Input Field    ${field_type}    ${field_value}
    END

    Submit Reference Form


Create A Reference Without Key
    [Arguments]    ${ref_type}    ${required_fields}
    Go To Create Page
    Select Reference Type    ${ref_type}

    FOR    ${field_type}    ${field_value}    IN    &{required_fields}
        Input Field    ${field_type}    ${field_value}
    END

    Submit Reference Form

Create A Reference Without Required Fields
    [Arguments]    ${ref_type}    ${ref_key}
    Go To Create Page
    Select Reference Type    ${ref_type}
    Input Reference Key    ${ref_key}

    Submit Reference Form