*** Settings ***
Documentation    Keywords for using the search/filter modal on the homepage.
...              Provides tools for searching by key, type, and field/value filters.

Resource         references.resource


*** Keywords ***
Filter By Key
    [Arguments]    ${key}
    Go To Homepage
    Open Search Window
    Input Search Key    ${key}
    Submit Search

Filter By Types
    [Arguments]    @{types}
    Go To Homepage
    Open Search Window
    Open Reference Type Dropdown
    FOR    ${type}    IN    @{types}
        Select Reference Type Option    ${type}
    END
    Close Reference Type Dropdown
    Submit Search

Filter By Field
    [Arguments]    ${field}    ${value}
    Go To Homepage
    Open Search Window
    Add Field Filter
    Set Field Filter    ${field}    ${value}
    Submit Search

