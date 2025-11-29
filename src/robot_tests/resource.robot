*** Settings ***
Library  SeleniumLibrary
Library  Collections

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
    [Arguments]  ${name}=Test dataset  ${type}=dataset  ${author}=Test Author  ${title}=Test Title  ${year}=2010  ${fields}={}
    Go To  ${HOME_URL}/add_reference

    Input Text  id=name  ${name}
    Input Text  id=author/editor  ${author}
    Input Text  id=title  Test ${title}
    Input Text  id=year/date  ${year}

    FOR  ${key}  ${value}  IN  @{fields}

        Select From List By Value  id=optional-select  ${key}
        Click Button  id=optional-button
        Wait Until Element Is Visible  name=${key}  10s
        Input Text  name=${key}  ${value}
    END

    Click Button  Submit  #Check for correct button type
    Wait Until Page Contains  ${name}


Verify Reference Is Visible
    [Arguments]  ${name}=Test dataset  ${type}=dataset  ${author}=Test Author  ${title}=Test Title  ${year}=2010  ${fields}={}
    Title Should Be  References
    Page Should Contain  ${name}
    Page Should Contain  type: ${type}
    Page Should Contain  author/editor: ${author}
    Page Should Contain  title: ${title}
    Page Should Contain  year/date: ${year}
    FOR  ${key}  ${value}  IN  @{fields}
        Page Should Contain  ${key}: ${value}
    END


Edit Reference
    [Arguments]  ${old_name}  ${new_values}
    Go To  ${HOME_URL}/references
    Click Element  xpath=//div[p[contains(text(), '${old_name}')]]//a[contains(@href, 'edit_reference')]
    
    FOR  ${key}  ${value}  IN  &{new_values}
        Run Keyword If  '${key}' == 'type'
            Select From List By Value  id=type  ${value}
        ELSE
            Input Text  id=${key}  ${value}
        END
    END
    
    Click Button  Submit  #Check for correct button type
    Wait Until Page Contains  ${new_values['name'] if 'name' in new_values else old_name}

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

Sort References
    [Arguments]  ${by}=title  ${order}=asc
    Select From List By Value  id=sort-select  ${by}
    Select From List By Value  id=order-select  ${order}
    Click Button  id=apply-sort
