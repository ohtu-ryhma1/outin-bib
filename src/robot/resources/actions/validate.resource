*** Settings ***
Documentation    High-level keywords for validating reference data using the card and form components.

Resource         ../components/card.resource
Resource         ../components/form.resource


*** Keywords ***
Reference Card Should Have Correct Data
    [Documentation]    Assert that the reference card displays the correct `ref_key`, `ref_type`, and `fields`.
    [Arguments]    ${ref_key}    ${ref_type}    ${fields}
    Reference Card Key Should Be    ${ref_key}    ${ref_key}
    Reference Card Type Should Be    ${ref_key}    ${ref_type}
    Reference Card Should Contain Fields    ${ref_key}    ${fields}

Reference Form Should Have Correct Data
    [Documentation]    Assert that the reference form displays the correct `ref_key`, `ref_type`, and `fields`.
    [Arguments]    ${ref_key}    ${ref_type}    ${fields}
    Reference Form Should Have Correct Key    ${ref_key}
    Reference Form Should Have Correct Type    ${ref_type}
    Reference Form Should Have Correct Fields    ${fields}
