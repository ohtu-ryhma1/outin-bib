*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Editing A Reference Succeeds
    Open And Configure Browser
    Create Reference
    Verify Reference Is Visible
    Click Edit Reference And Check The Content

    Select From List By Value  id=type  online

    #Checking that old information is not visible
    Element Attribute Value Should Be  id=name  value  ${EMPTY}
    Element Attribute Value Should Be  id=author  value  ${EMPTY}
    Element Attribute Value Should Be  id=title  value  ${EMPTY}
    Element Attribute Value Should Be  id=year/date  value  ${EMPTY}
    Element Attribute Value Should Be  id=eprint  value   ${EMPTY}

    Input Text  id=name  TestName
    Input Text  id=author  AuthorTest
    Input Text  id=editor  EditorTest
    Input Text  id=title  TitleTest
    Input Text  id=year/date  2010
    Input Text  id=doi  DoiTest
    Input Text  id=eprint  EprintTest
    Input Text  id=url  TestUrl

    Click Button  Submit

    #Checking that there is new information
    Page Should Contain  @TestName
    Page Should Contain  AuthorTest
    Page Should Contain  EditorTest
    Page Should Contain  TitleTest
    Page Should Contain  2010
    Page Should Contain  DoiTest
    Page Should Contain  EprintTest
    Page Should Contain  TestUrl

Editing A Reference Fails:
    Open And Configure Browser
    Create Reference
    Verify Reference Is Visible
    Click Edit Reference And Check The Content

    Select From List By Value  id=type  suppbook

    Input Text  id=booktitle  BookTitleTest
    Input Text  id=year/date  1900

    Click Button  Submit

    #Checking that the submission doesn't go through
    Element Should Be Visible  id=booktitle
    Element Should Be Visible  id=year/date

    Input Text  id=name  SuppBookName

    Click Button  Submit

    Page Should Contain  @SuppBookName
    Page Should Contain  BookTitleTest
    Page Should Contain  1900
