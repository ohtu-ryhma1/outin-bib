*** Settings ***
Documentation    Intermediate level keywords for interacting with the reference form component.

Resource    ../shared/ui.resource


*** Variables ***
${INPUT_REF_KEY}        id:ref-key-input
${SELECT_REF_TYPE}      id:ref-type-select
${SELECT_FIELD_TYPE}    id:field-select
${BUTTON_ADD_FIELD}     id:add-field-button
${BUTTON_SUBMIT}        id:submit


*** Keywords ***
Input Reference Key
    [Documentation]    Input the `ref_key` into the form.
    [Arguments]    ${ref_key}
    UI Input Text    ${INPUT_REF_KEY}    ${ref_key}

Select Reference Type
    [Documentation]    Select the `ref_type` from the dropdown.
    [Arguments]    ${ref_type}
    UI Select Option    ${SELECT_REF_TYPE}    ${ref_type}

Input Field
    [Documentation]    Input the `field_value` of a specific `field_type`.
    [Arguments]    ${field_type}    ${field_value}
    UI Input Text    id:${field_type}    ${field_value}

Add Field
    [Documentation]    Add a certain `field_type` to the form.
    [Arguments]    ${field_type}
    UI Select Option   ${SELECT_FIELD_TYPE}    ${field_type}
    Click Button    ${BUTTON_ADD_FIELD}

Does Field Exist
    [Documentation]    Check if a certain `field_type` exists on the form.
    [Arguments]    ${field_type}
    ${field_exists} =    Run Keyword And Return Status    UI Element Should Be Visible    id:${field_type}
    RETURN    ${field_exists}

Submit Reference Form
    [Documentation]    Submit the reference form.
    Scroll Element Into View    ${BUTTON_SUBMIT}
    Click Button    ${BUTTON_SUBMIT}

Reference Form Should Have Correct Key
    [Documentation]    Assert that the reference form has the correct `ref_key`.
    [Arguments]    ${ref_key}
    UI Element Value Should Be    ${INPUT_REF_KEY}    ${ref_key}

Reference Form Should Have Correct Type
    [Documentation]    Assert that the reference form has the correct `ref_type`.
    [Arguments]    ${ref_type}
    UI Element Should Contain    ${SELECT_REF_TYPE}    ${ref_type}

Reference Form Should Have Correct Fields
    [Documentation]    Assert that the reference form has the correct `fields`.
    [Arguments]    ${fields}
    FOR    ${field_type}    ${field_value}    IN    &{fields}
        UI Element Should Contain    id:${field_type}    ${field_value}
    END
