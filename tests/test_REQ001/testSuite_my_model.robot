*** Settings ***
Documentation     Test suite to validate my_model.slx.
...
...               Keywords are imported from the resource file
Resource          keywords_my_model.resource
Default Tags      positive

*** Variables ***
@{input}    ${1}    ${2}    ${4}    ${5}    ${10}    ${0}    ${-1}

*** Test Cases ***
Validate My Model
    [Tags]    REQ001
    [Documentation]    Test My Model
    Check My Model    ${input}