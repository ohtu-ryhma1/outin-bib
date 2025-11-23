*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Creating a reference succeeds
    Go To  ${HOME_URL}
    Click Link  Add a new reference
    Title Should Be  Create a new reference

    Select From List By Value  id=type  book

    Page Should Contain  Required Fields:
    Input Text  id=name  Test Book
    Input Text  id=author  Test Author
    Input Text  id=title  Test Title
    Input Text  id=year/date  2025

    Page Should Contain  Optional Fields:

    Select From List By Value  id=optional-select  editor
    Click Button  id=optional-button
    Wait Until Element Is Visible  name=editor  5s
    Input Text  name=editor  EditorNimi

    Select From List By Value  id=optional-select  translator
    Click Button  id=optional-button
    Wait Until Element Is Visible  name=translator  5s
    Input Text  name=translator  TranslatorNimi

    Click Button  Submit

    Title Should Be  References
    Page Should Contain  Test Book, type: book
    Page Should Contain  author: Test Author
    Page Should Contain  title: Test Title
    Page Should Contain  year/date: 2025
    Page Should Contain  editor: EditorNimi
    Page Should Contain  translator: TranslatorNimi

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