*** Settings ***
Library            OperatingSystem
Library            ../libraries/app_library.py
Library            ../libraries/file_export_library.py

Resource          ../resources/shared/browser.resource
Resource          ../resources/references/import_export.resource
Resource          ../resources/references/references.resource
Resource          ../resources/references/create.resource
Resource          ../resources/references/verify.resource

Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset Db

*** Variables ***
&{DICT_BOOK}       author=test_author    title=test_title    year/date=test_year/date
&{DICT_ARTICLE}    author=testAuthor     title=testTitle     journaltitle=journalTitle    year/date=test_year_article
${DOWNLOAD_DIR}    Evaluate    os.path.abspath('downloads')    modules=os
${FILE_NAME}       references.bib
${FILE_PATH}       ${DOWNLOAD_DIR}/${FILE_NAME}

*** Test Cases ***
Import Export Page Is Accessible
    Go To Import Export Page
    Import Export Page Should Be Open

Export Empty Reference To Copy Succeeds
    Go To Import Export Page
    Click Export Copy Button
    Handle Alert  ACCEPT
    ${export_text}=  Get Value  ${EXPORT_TEXTAREA}
    Should Be Empty  ${export_text}  

Export Single Reference To Copy Succeeds
    Go To Import Export Page
    Create A Reference    book    test_key    ${DICT_BOOK}
    Go To Import Export Page
    Click Export Copy Button
    Handle Alert  ACCEPT
    ${export_text}=  Get Value  ${EXPORT_TEXTAREA}
    Should Contain  ${export_text}  ${DICT_BOOK.author}
    Should Contain  ${export_text}  ${DICT_BOOK.title}

Export Multiple Reference To Copy Succeeds
    Create A Reference    book    book_key    ${DICT_BOOK}
    Create A Reference    article    article_key    ${DICT_ARTICLE}
    Go To Import Export Page
    Click Export Copy Button
    Handle Alert  ACCEPT
    ${export_text}=  Get Value  ${EXPORT_TEXTAREA}
    Should Contain  ${export_text}  ${DICT_BOOK.author}
    Should Contain  ${export_text}  ${DICT_BOOK.title}
    Should Contain  ${export_text}  ${DICT_ARTICLE.author}
    Should Contain  ${export_text}  ${DICT_ARTICLE.title}
    Should Contain  ${export_text}  ${DICT_ARTICLE.journaltitle}

Export Reference File Works Without Browser
    FileExport.Download Reference File    ${HOME_URL}    ${FILE_PATH}
    FileExport.File Should Exist    ${FILE_PATH}

    ${content}=    Get File    ${FILE_PATH}
    Should Contain    ${content}    @