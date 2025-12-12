*** Settings ***
Documentation    Intermediate level keywords for interacting with flash messages.

Resource          ../shared/ui.resource


*** Keywords ***
Wait Until Flash Message Is Visible
    [Documentation]    Verifies that a flash message is visible on the page.
    UI Wait Until Element Is Visible    css:.flash-message

Wait Until Flash Message Contains
    [Documentation]    Verifies that the flash message contains the expected text.
    [Arguments]    ${expected_text}
    ${flash_text}=    UI Get Text    css:.flash-message
    Should Contain    ${flash_text}    ${expected_text}
