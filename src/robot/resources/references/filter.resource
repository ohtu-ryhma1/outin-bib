Filter By Name
    [Arguments]  ${name}
    Input Text  id=search-bar  ${name}
    Press Key  id=search-bar  ENTER
    Wait Until Page Contains  ${name}


Filter By Type
    [Arguments]  ${type}
    Input Text  id=search-bar  ${type}
    Press Key  id=search-bar  ENTER
    Wait Until Page Contains  ${type}


Filter By Field
    [Arguments]  ${field_type}
    Select From List By Value  id=field-filter-select  ${field_type}
    Click Button  id=apply-filter


Filter By Field Value
    [Arguments]  ${field_type}  ${value}
    Select From List By Value  id=field-select  ${field_type}
    Input Text  id=field-value-input  ${value}
    Click Button  id=apply-filter
    Wait Until Page Contains  ${value}

Sort References
    [Arguments]  ${by}=title  ${order}=asc
    Select From List By Value  id=sort-select  ${by}
    Select From List By Value  id=order-select  ${order}
    Click Button  id=apply-sort
