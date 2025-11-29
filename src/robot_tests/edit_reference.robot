*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Editing A Reference Succeeds
    Create Reference
    Verify Reference Is Visible

    Edit Reference  Test dataset  new_values={
    ...    'name':'TestName',
    ...    'author/editor':'AuthorTest',
    ...    'editor':'EditorTest',
    ...    'title':'TitleTest',
    ...    'year/date':'2010',
    ...    'doi':'DoiTest',
    ...    'eprint':'EprintTest',
    ...    'url':'TestUrl'
    ...    }

    Verify Reference Is Visible  TestName  dataset  AuthorTest  TitleTest  2010  {'doi':'DoiTest', 'eprint':'EprintTest', 'url':'TestUrl'}

Editing A Reference Fails:
    Create Reference
    Verify Reference Is Visible

    Edit Reference  Test dataset  new_values={
    ...    'type':'suppbook',
    ...    'booktitle':'BookTitleTest',
    ...    'year/date':'1900'
    ...    }

    #Checking that the submission doesn't go through
    Element Should Be Visible  id=booktitle
    Element Should Be Visible  id=year/date

    Edit Reference  Test dataset  new_values={
    ...    'type':'suppbook',
    ...    'name':'SuppBookName',
    ...    'booktitle':'BookTitleTest',
    ...    'year/date':'1900'
    ...    }

    Verify Reference Is Visible  SuppBookName  suppbook  Test Author  Test Title  1900  {'booktitle':'BookTitleTest'}
