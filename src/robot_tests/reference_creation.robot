*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Creating a reference succeeds
    Open And Configure Browser
    Create Reference
    Verify Reference Is Visible

Creating a reference fails
    Go To  ${HOME_URL}
    Click Link  Add a new reference
    Title Should Be  Create a new reference

    Select From List By Value  id=type  mvbook

    Page Should Contain  Required Fields:
    Input Text  id=name  Test2
    Input Text  id=author  TestAuthor2

    Page Should Contain  Optional Fields:

    Select From List By Value  id=optional-select  subtitle
    Click Button  id=optional-button
    Wait Until Element Is Visible  name=subtitle  5s
    Input Text  name=subtitle  SubTiName

    Select From List By Value  id=optional-select  series
    Click Button  id=optional-button
    Wait Until Element Is Visible  name=series  5s
    Input Text  name=series  SeriesName

    Click Button  Submit

    Element Should Be Visible  id=type
    Element Should Be Visible  id=name

    Input Text  id=title  TestTitle2

    Click Button  Submit

    Element Should Be Visible  id=type
    Element Should Be Visible  id=name


    Click Button  Submit

Not adding Reference name fails
    Go To  ${HOME_URL}
    Click Link  Add a new reference
    Title Should Be  Create a new reference

    Select From List By Value  id=type  book

    Page Should Contain  Required Fields:
    Input Text  id=author  Fail
    Input Text  id=title  Test Fail
    Input Text  id=year/date  202

    Click Button  Submit

    Element Should Be Visible  id=type
    Element Should Be Visible  id=author