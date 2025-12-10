*** Settings ***
Documentation    High-level keywords for searching references using the search component.

Resource         ../components/search.resource
Resource         ../components/card.resource


*** Keywords ***
Search References
    [Documentation]    Search references by a given `key`, list of `types` and dictionary of `filters` using the search component.
    [Arguments]    ${key}=${None}   ${types}=@{EMPTY}    ${filters}=&{EMPTY}
    Open Search Window
    IF    $key != $None
        Input Search Key    ${key}
    END

    FOR    ${type}    IN    @{types}
        Open Reference Type Dropdown
        Add Reference Type    ${type}
    END
    Close Reference Type Dropdown

    FOR    ${field_name}    ${field_value}    IN    &{filters}
        Add Field Filter
        Set Field Filter    ${field_name}    ${field_value}
    END

    Submit Search
