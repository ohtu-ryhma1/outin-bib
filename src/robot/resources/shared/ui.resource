*** Settings ***
Documentation       Low-level keywords for interacting with the website.

Library             SeleniumLibrary


*** Keywords ***
UI Click Element
    [Documentation]    Wait until the element is visible, scroll it into view, and click it using the given `locator`.
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}
    Scroll Element Into View    ${locator}
    Click Element    ${locator}

UI Input Text
    [Documentation]    Wait until the element is visible, scroll it into view, and input the given `text` at the input at `locator`.
    [Arguments]    ${locator}    ${text}
    Wait Until Element Is Visible    ${locator}
    Scroll Element Into View    ${locator}
    Input Text    ${locator}    ${text}

UI Select Option
    [Documentation]    Wait until the element is visible, scroll it into view, and select the given `option` from the dropdown at `locator`.
    [Arguments]    ${locator}    ${option}
    Wait Until Element Is Visible    ${locator}
    Scroll Element Into View    ${locator}
    Select From List By Label    ${locator}    ${option}

UI Wait Until Element Is Visible
    [Documentation]    Wait until the element at `locator` is visible.
    [Arguments]    ${locator}
    Wait Until Element Is Visible   ${locator}    timeout=3s

UI Wait Until Element Is Not Visible
    [Documentation]    Wait until the element at `locator` is not visible.
    [Arguments]    ${locator}
    Wait Until Element Is Not Visible    ${locator}    timeout=3s

UI Element Should Be Visible
    [Documentation]    Assert that the element at `locator` is visible.
    [Arguments]    ${locator}
    Element Should Be Visible    ${locator}

UI Element Should Not Be Visible
    [Documentation]    Assert that the element at `locator` is not visible.
    [Arguments]    ${locator}
    Element Should Not Be Visible    ${locator}

UI Element Should Contain
    [Documentation]    Wait until the element at `locator` is visible and assert that it contains the given `text`.
    [Arguments]    ${locator}    ${text}
    Wait Until Element Is Visible    ${locator}
    Element Should Contain    ${locator}    ${text}

UI Element Value Should Be
    [Documentation]    Wait until the element at `locator` is visible and assert that its value is equal to `value`.
    [Arguments]    ${locator}    ${value}
    Wait Until Element Is Visible    ${locator}
    Element Attribute Value Should Be    ${locator}    value    ${value}

UI Get WebElement
    [Documentation]    Wait until the element at `locator` is visible and return the WebElement.
    [Arguments]    ${locator}
    UI Wait Until Element Is Visible    ${locator}
    ${element} =    Get WebElement    ${locator}
    RETURN    ${element}

UI Press Key
    [Documentation]    Press the given `key`.
    [Arguments]    ${key}
    Press Keys    ${None}    ${key}

UI Choose File
    [Documentation]    Upload a file located at `file_path` to the input at `locator`.
    [Arguments]    ${locator}    ${file_path}
    Choose File    ${locator}    ${file_path}
