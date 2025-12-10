*** Settings ***
Documentation       Intermediate level keywords for interacting with reference card components.

Resource          ../shared/ui.resource


*** Keywords ***
Get Reference Card Webelement
    [Documentation]    Get the WebElement of the reference card with a given `ref_key`.
    [Arguments]    ${ref_key}
    UI Wait Until Element Is Visible    xpath://a[@class='ref-card' and .//p[text()='${ref_key}']]
    ${ref_card} =    Get Webelement    xpath://a[@class='ref-card' and .//p[text()='${ref_key}']]
    RETURN    ${ref_card}

Click Reference Card
    [Documentation]    Click a reference card with a given `ref_key`.
    [Arguments]    ${ref_key}
    ${ref_card} =    Get Reference Card Webelement    ${ref_key}
    UI Click Element    ${ref_card}

Reference Card Should Be Visible
    [Documentation]    Assert that the reference card with a given `ref_key` is visible.
    [Arguments]    ${ref_key}
    UI Wait Until Element Is Visible    xpath://a[@class='ref-card' and .//p[text()='${ref_key}']]

Reference Card Should Not Be Visible
    [Documentation]    Assert that the reference card with a given `ref_key` is not visible.
    [Arguments]    ${ref_key}
    UI Wait Until Element Is Not Visible    xpath://a[@class='ref-card' and .//p[text()='${ref_key}']]

Reference Card Key Should Be
    [Documentation]    Assert that the reference card with a given `ref_key` has the expected `key`.
    [Arguments]    ${ref_key}    ${key}
    ${ref_card} =    Get Reference Card Webelement    ${ref_key}
    UI Element Should Contain    ${ref_card}    ${key}

Reference Card Type Should Be
    [Documentation]    Assert that the reference card with a given `ref_key` has the given `type`.
    [Arguments]    ${ref_key}    ${type}
    ${ref_card} =    Get Reference Card Webelement    ${ref_key}
    UI Element Should Contain    ${ref_card}    ${type}

Reference Card Should Contain Fields
    [Documentation]    Assert that the reference card with a given `ref_key` contains all the specified `fields`.
    [Arguments]    ${ref_key}    ${fields}
    ${ref_card} =    Get Reference Card Webelement    ${ref_key}

    FOR    ${field_type}    ${field_value}    IN    &{fields}
        UI Element Should Contain    ${ref_card}    ${field_type}
        UI Element Should Contain    ${ref_card}    ${field_value}
    END
