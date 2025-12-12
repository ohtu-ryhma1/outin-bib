*** Settings ***
Library            OperatingSystem
Library            ../libraries/repository_api.py
Library            ../libraries/file_api.py

Resource          ../resources/shared/browser.resource
Resource          ../resources/actions/export.resource

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Db And Clear Downloads And Go To Export Page


*** Variables ***
${URL_EXPORT}       import-export

&{FIELDS_1}         author=test_author      title=test_title      year/date=test_year/date
&{FIELDS_2}         author=test_author_2    title=test_title_2    year/date=test_year/date_2


*** Test Cases ***
Page Text Is Empty With No References
    ${text} =    Get Exported Text From Page
    Should Be Empty    ${text}

Clipboard Text Is Empty With No References
    Skip If    ${HEADLESS}    Clipboard API is not supported in headless mode
    ${text} =    Get Exported Text From Clipboard
    Should Be Empty    ${text}

File Is Empty With No References
    Export File
    ${download_dir} =    Normalize Path    ${DOWNLOAD_DIR}
    ${export_file} =    Wait Until Keyword Succeeds    5s    0.5s    Get Latest Exported File Path   ${download_dir}
    ${file_content} =    Get File    ${export_file}
    Should Be Empty    ${file_content}

Page Text Has Correct Reference
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Reload Page
    ${text} =    Get Exported Text From Page
    Should Contain    ${text}       test_author

Clipboard Text Has Correct Reference
    Skip If    ${HEADLESS}    Clipboard API is not supported in headless mode
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Reload Page
    ${text} =    Get Exported Text From Clipboard
    Should Contain    ${text}    test_author

File Has Correct Reference
    Create Reference Via Request    book    test_key    ${FIELDS_1}
    Reload Page
    Export File
    ${download_dir} =    Normalize Path    ${DOWNLOAD_DIR}
    ${export_file} =    Wait Until Keyword Succeeds    5s    0.5s    Get Latest Exported File Path    ${download_dir}
    ${file_content} =    Get File    ${export_file}
    Should Contain    ${file_content}    test_author


*** Keywords ***
Reset Db And Clear Downloads And Go To Export Page
    Reset Db
    Clear Download Directory
    Go To Page    ${URL_EXPORT}
