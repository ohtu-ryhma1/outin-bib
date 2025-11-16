*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Application

*** Test Cases ***
No references at the beginning
    Go To  ${HOME_URL}
    Title Should Be  References
    Page Should Contain  No references

Creating a reference succeeds
    Go To  ${HOME_URL}
    Click Link  Add a new reference
    Title Should Be  Create a new reference
    Select From List By Value  type  article
    Input Text  name  Test Reference 1
    Input Text  title  Test Title 1
    Input Text  author  Test Author 1
    Click Button  Submit
    Title Should Be  References
    Page Should Contain  Test Reference 1, type: article