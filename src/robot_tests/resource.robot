*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.5 seconds
${HOME_URL}   http://${SERVER}
${BROWSER}    chrome
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
        Call Method  ${options}  add_argument  --incognito
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
        Call Method  ${options}  add_argument  --private-window
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0.01 seconds
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}


Create Reference
    Go To  ${HOME_URL}
    Click Link  Add a new reference
    Title Should Be  Create a new reference

    Select From List By Value  id=type  dataset

    Page Should Contain  Required Fields:

    Element Should Be Visible  id=name
    Element Should Be Visible  id=author/editor
    Element Should Be Visible  id=title
    Element Should Be Visible  id=year/date

    Input Text  id=name  Test dataset
    Input Text  id=author/editor  Test Author
    Input Text  id=title  Test Title
    Input Text  id=year/date  2010

    Page Should Contain  Optional Fields:
    Page Should Contain  No optional fields added

    Select From List By Value  id=optional-select  eprint
    Click Button  id=optional-button
    Wait Until Element Is Visible  name=eprint  10s
    Input Text  name=eprint  EprintName

    Select From List By Value  id=optional-select  publisher
    Click Button  id=optional-button
    Wait Until Element Is Visible  name=publisher
    Input Text  name=publisher  PublisherName

    Click Button  Submit

Verify Reference Is Visible
    Title Should Be  References
    Page Should Contain  Test dataset, type: dataset
    Page Should Contain  author/editor: Test Author
    Page Should Contain  title: Test Title
    Page Should Contain  year/date: 2010
    Page Should Contain  eprint: EprintName
    Page Should Contain  publisher: PublisherName
