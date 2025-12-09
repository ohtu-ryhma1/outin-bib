*** Settings ***
Library    SeleniumLibrary
Library    ../../libraries/file_export_library.py


*** Variables ***
${SERVER}        localhost:5001
${HOME_URL}      http://${SERVER}
${BROWSER}       chrome
${HEADLESS}      false
${DELAY}         0.1 seconds
${DOWNLOAD_DIR}  ${CURDIR}${/}downloads
${FILE_PATH}     ${DOWNLOAD_DIR}/references.bib

*** Keywords ***
Setup Suite
    Remove Directory    ${DOWNLOAD_DIR}    recursive=True
    Create Directory    ${DOWNLOAD_DIR}
    Set Download Directory
    Open And Configure Browser

Set Download Directory
    ${download}=    Normalize Path    ${CURDIR}/../downloads
    Remove Directory    ${download}    recursive=True
    Create Directory    ${download}
    Set Suite Variable    ${DOWNLOAD_DIR}    ${download}
    Set Suite Variable    ${FILE_PATH}       ${download}${/}references.bib

Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
        Call Method  ${options}  add_argument  --incognito
        ${prefs}=  Create Dictionary
        ...    download.default_directory=${DOWNLOAD_DIR}
        ...    download.prompt_for_download=False
        ...    download.directory_upgrade=True
        Call Method  ${options}  add_experimental_option  prefs  ${prefs}
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
        Call Method  ${options}  add_argument  --private-window
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0 seconds
        Call Method  ${options}  add_argument  --headless
        Set Selenium Speed 0 seconds
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  ${HOME_URL}  ${BROWSER}  options=${options}
    Maximize Browser Window

Wait For Downloaded File
    [Arguments]    ${download_dir}    ${expected_name}    ${timeout}=30
    ${end_time}=    Evaluate    time.time() + ${timeout}    modules=time

    FOR    ${index}    IN RANGE    1000
        ${files}=    List Files In Directory    ${download_dir}
        ${tmp_files}=    Evaluate    [f for f in ${files} if f.endswith('.tmp')]
        Run Keyword If    not ${tmp_files}    Exit For Loop
        Run Keyword If    time.time() > ${end_time}    Fail    Download did not complete within ${timeout} seconds
        Sleep    0.5s
    END

    ${files}=    List Files In Directory    ${download_dir}
    ${matches}=    Evaluate    [f for f in ${files} if f == '${expected_name}']
    Should Not Be Empty    ${matches}
