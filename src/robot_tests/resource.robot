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
    Click Element  css:a.nav-link[href='/new_reference']
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
    Page Should Contain  @Test dataset
    Page Should Contain  Test Author
    Page Should Contain  Test Title
    Page Should Contain  2010
    Page Should Contain  EprintName
    Page Should Contain  PublisherName


Click Edit Reference And Check The Content
    Click Element  css:a.icon-link

    Element Attribute Value Should Be  id=name  value  Test dataset
    Element Attribute Value Should Be  id=author/editor  value  Test Author
    Element Attribute Value Should Be  id=title  value  Test Title
    Element Attribute Value Should Be  id=year/date  value  2010
    Element Attribute Value Should Be  id=eprint  value  EprintName
    Element Attribute Value Should Be  id=publisher  value  PublisherName


Filter By Name
    [Arguments]  ${name}
    Input Text  id=search-bar  ${name}
    Press Key  id=search-bar  ENTER
    Wait Until Page Contains  ${name}


Filter By Type
    [Arguments]  ${type}
    Input Text  id=search-bar  ${type}
    Press Key  id=search-bar  ENTER
    Wait Until Page Contains  ${type}


Filter By Field
    [Arguments]  ${field_type}
    Select From List By Value  id=field-filter-select  ${field_type}
    Click Button  id=apply-filter


Filter By Field Value
    [Arguments]  ${field_type}  ${value}
    Select From List By Value  id=field-select  ${field_type}
    Input Text  id=field-value-input  ${value}
    Click Button  id=apply-filter
    Wait Until Page Contains  ${value}