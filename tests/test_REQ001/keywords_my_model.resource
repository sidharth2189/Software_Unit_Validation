*** Settings ***
Documentation     This is a resource file, that can contain variables and keywords.
...               Keywords defined here can be used where this Keywords.resource in loaded.
Library           input_my_model.py
Library           Collections

*** Variables ***
${gain}    ${2}
@{expected}

*** Keywords ***
Check My Model
    [Arguments]    ${inp}
    @{result}    Test My Model    ${inp}
    FOR    ${element}    IN    @{inp}
        ${out}    Evaluate    ${gain} * ${element}
        Append To List    ${expected}    ${out}
    END
    Should Be Equal    ${result}     ${expected}
