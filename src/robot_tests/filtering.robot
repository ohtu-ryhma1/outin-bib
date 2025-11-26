*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Filter By Name Works
    Create Reference
    Verify Reference Is Visible
    Filter By Name  Test dataset
    Page Should Contain  Test dataset

Filter By Type Works
    Create Reference
    Verify Reference Is Visible
    Filter By Type  dataset
    Page Should Contain  dataset

Filter By Field Works
    Create Reference
    Verify Reference Is Visible
    Filter By Field  eprint
    Page Should Contain  EprintName

Filter By Field Value Works
    Create Reference
    Verify Reference Is Visible
    Filter By Field Value  publisher  PublisherName
    Page Should Contain  PublisherName
