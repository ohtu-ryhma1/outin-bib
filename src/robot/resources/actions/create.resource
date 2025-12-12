*** Settings ***
Documentation    High-level keywords for creating references using the form component.

Resource    ../components/form.resource


*** Keywords ***
Create Reference
    [Documentation]    Create a reference with a given `ref_type`, `ref_key` and `fields` using the form component.
    [Arguments]    ${ref_type}=${None}    ${ref_key}=${None}    ${fields}=&{EMPTY}

    IF    $ref_type != $None
        Select Reference Type    ${ref_type}
    END

    IF    $ref_key != $None
        Input Reference Key    ${ref_key}
    END

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
