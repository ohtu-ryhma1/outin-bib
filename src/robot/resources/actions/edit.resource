*** Settings ***
Documentation    High-level keywords for editing references using the form component.

Resource    ../components/form.resource


*** Keywords ***
Edit Reference
    [Documentation]    Edit an existing reference with a given `ref_key` with `new_ref_key` and `new_fields`.
    [Arguments]    ${ref_key}    ${new_ref_key}=${None}    ${new_fields}=&{EMPTY}
    IF    $new_ref_key
        Input Reference Key    ${new_ref_key}
    END

    FOR    ${field_type}    ${field_value}    IN    &{new_fields}
        ${field_exists} =    Does Field Exist    ${field_type}
        IF    ${field_exists}
            Input Field    ${field_type}    ${field_value}
        ELSE
            Add Field    ${field_type}
            Input Field    ${field_type}    ${field_value}
        END
    END

    Submit Reference Form
