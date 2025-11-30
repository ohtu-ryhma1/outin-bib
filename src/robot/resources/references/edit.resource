*** Settings ***
Documentation    This file provides keywords to edit references
...              with different configurations

Resource    references.resource

*** Keywords ***
Edit Reference
    [Arguments]    ${ref_key}    ${new_ref_key}    ${fields}
    Go To Edit Page    ${ref_key}
    Edit Page Should Be Open
    Input Reference Key    ${new_ref_key}

    FOR    ${field_type}    ${field_value}    IN    &{fields}
        ${field_exists} =    Does Field Exist    ${field_type}
        IF    ${field_exists}
            Input Field    ${field_type}    ${field_value}
        ELSE
            Add Field    ${field_type}
            Input Field    ${field_type}    ${field_value}
        END
    END

    Submit Reference Form
