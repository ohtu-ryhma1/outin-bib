*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Application

*** Test Cases ***
Creating a reference succeeds
    Go To  ${HOME_URL}
    Click Link  Add a new reference
    Title Should Be  Create a new reference

    Select From List By Value  id=type  book

    #Pakolliset
    Input Text  id=name  Test Book
    Input Text  id=author  Test Author
    Input Text  id=title  Test Title
    Input Text  id=year/date  2025

    Page Should Contain  Optional Fields:

    #Valinnaiset
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
########

Creating a reference fails 
    Go To  ${HOME_URL}
    Click Link  Add a new reference
    Title Should Be  Create a new reference
    Select From List By Value  type  mvbook
    Page Should Contain  eprint
    Input Text  name  TestMVbook
    Input Text  title  TitleMVBook
    Input Text  titleaddon  TitleAddonTest
    Click Button  Submit