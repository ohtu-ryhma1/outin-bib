*** Settings ***
Documentation     High-level keywords for importing data using the import component.

Resource          ../components/import.resource


*** Keywords ***
Import From Text
    [Documentation]    Import data from a given `text`.
    [Arguments]    ${text}
    Input Import Text    ${text}
    Submit Import From Text

Import From File
    [Documentation]    Import data from a file located at `file_path`.
    [Arguments]    ${file_path}
    Upload Import File    ${file_path}
    Submit Import From File
