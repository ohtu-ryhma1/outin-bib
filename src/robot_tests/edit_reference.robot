*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Creating a reference succeeds
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

    Title Should Be  References
    Page Should Contain  @Test dataset
    Page Should Contain  Test Author
    Page Should Contain  Test Title
    Page Should Contain  2010
    Page Should Contain  EprintName
    Page Should Contain  PublisherName

    #Edit the reference
    Click Element  css:a.icon-link

    #Checking that prior information is visible
    Element Attribute Value Should Be  id=name  value  Test dataset
    Element Attribute Value Should Be  id=author/editor  value  Test Author
    Element Attribute Value Should Be  id=title  value  Test Title
    Element Attribute Value Should Be  id=year/date  value  2010
    Element Attribute Value Should Be  id=eprint  value  EprintName
    Element Attribute Value Should Be  id=publisher  value  PublisherName

    Select From List By Value  id=type  online
    
    #Checking that old information is not visible
    Element Attribute Value Should Be  id=name  value  ${EMPTY}
    Element Attribute Value Should Be  id=author  value  ${EMPTY}
    Element Attribute Value Should Be  id=title  value  ${EMPTY}
    Element Attribute Value Should Be  id=year/date  value  ${EMPTY}
    Element Attribute Value Should Be  id=eprint  value   ${EMPTY}

    Input Text  id=author  AuthorTest
    Input Text  id=editor  EditorTest
    Input Text  id=title  TitleTest
    Input Text  id=year/date  2010
    Input Text  id=doi  DoiTest
    Input Text  id=eprint  EprintTest
    Input Text  id=url  TestUrl

    Click Button  Submit
    
    #Checking that the submission doesnt go through
    Element Should Be Visible  id=author
    Element Should Be Visible  id=editor
    Element Should Be Visible  id=title
    Element Should Be Visible  id=year/date
    Element Should Be Visible  id=doi
    Element Should Be Visible  id=eprint
    Element Should Be Visible  id=url

    Input Text  id=name  TestName

    Click Button  Submit

    Page Should Contain  @TestName
    Page Should Contain  AuthorTest
    Page Should Contain  EditorTest
    Page Should Contain  TitleTest
    Page Should Contain  2010
    Page Should Contain  DoiTest
    Page Should Contain  EprintTest
    Page Should Contain  TestUrl