*** Settings ***
Library    SeleniumLibrary
Library    file_export_library.py


*** Variables ***
${SERVER}        localhost:5001
${HOME_URL}      http://${SERVER}
${BROWSER}       chrome
${HEADLESS}      false
${DELAY}         0.1 seconds
${DOWNLOAD_DIR}  ${EXECDIR}/downloads
${FILE_PATH}     ${DOWNLOAD_DIR}/references.bib


*** Keywords ***
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
