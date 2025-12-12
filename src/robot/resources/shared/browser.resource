*** Settings ***
Documentation    Low level keywords for configuring and interacting with the browser.

Library          OperatingSystem
Library          SeleniumLibrary


*** Variables ***
${URL_SERVER}      http://localhost:5001
${DOWNLOAD_DIR}    ${CURDIR}/../../data/downloads
${BROWSER}         chrome
${HEADLESS}        ${False}


*** Keywords ***
Go To Homepage
    Go To    ${URL_SERVER}

Go To Page
    [Arguments]    ${url}
    Go To    ${URL_SERVER}/${url}

Reload Page
    SeleniumLibrary.Reload Page

Wait Until Page Is Homepage
    Wait Until Location Contains    ${URL_SERVER}    timeout=3s

Wait Until Page Is Open
    [Arguments]    ${url}
    Wait Until Location Contains    ${url}    timeout=3s

Clear Download Directory
    Remove Directory    ${DOWNLOAD_DIR}    recursive=True
    Create Directory    ${DOWNLOAD_DIR}

Open And Configure Browser
    [Arguments]    ${headless}=${HEADLESS}    ${browser}=${BROWSER}    ${url}=${URL_SERVER}
    ${download_dir} =    Normalize Path    ${DOWNLOAD_DIR}

    IF    '${browser}' == 'chrome'
        ${prefs} =    Create Dictionary    download.default_directory=${download_dir}
        ${chrome_options} =    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
        Call Method    ${chrome_options}    add_experimental_option    prefs    ${prefs}
        Run Keyword If    ${HEADLESS}    Call Method    ${chrome_options}    add_argument    --headless
        Open Browser    ${url}    chrome    options=${chrome_options}
    ELSE IF    '${browser}' == 'firefox'
        ${ff_options} =    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys, selenium.webdriver
        Call Method    ${ff_options}    set_preference    browser.download.folderList    2
        Call Method    ${ff_options}    set_preference    browser.download.dir    ${download_dir}
        Run Keyword If    ${HEADLESS}    Call Method    ${ff_options}    add_argument    --headless
        # Call Method    ${ff_options}    set_preference    browser.helperApps.neverAsk.saveToDisk    application/octet-stream,application/pdf,text/x-bibtex,application/x-bibtex
        # Call Method    ${ff_options}    set_preference    browser.download.manager.showWhenStarting    False
        # Call Method    ${ff_options}    set_preference    pdfjs.disabled    True
        Open Browser    ${url}    firefox    options=${ff_options}
    ELSE
        Fail    Unsupported browser: ${browser}
    END
