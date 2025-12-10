*** Settings ***
Documentation       Low level keywords for interacting with the browser.

Library             SeleniumLibrary


*** Variables ***
${BROWSER}     chrome
${HEADLESS}    false
${DELAY}       0

${URL_SERVER}    localhost:5001
${URL_HOME}      http://${URL_SERVER}


*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options} =    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
        Call Method    ${options}    add_argument    --incognito
    ELSE IF  $BROWSER == 'firefox'
        ${options}    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys
        Call Method    ${options}    add_argument    --private-window
    END

    IF  $HEADLESS == 'true'
        Call Method    ${options}     add_argument    --headless
    ELSE
        Set Selenium Speed    ${DELAY}
    END

    Open Browser    browser=${BROWSER}    options=${options}

Go To Homepage
    Go To    ${URL_HOME}

Go To Page
    [Arguments]    ${url}
    Go To    ${URL_HOME}/${url}

Homepage Should Be Open
    Location Should Contain    ${URL_HOME}

Page Should Be Open
    [Arguments]    ${url}
    Location Should Contain    ${url}
