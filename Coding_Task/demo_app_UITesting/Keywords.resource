*** Settings ***
Documentation     Resource file to define keywords used in the project
Library           SeleniumLibrary  
Resource          Common.resource  


*** Keywords ***
Initiate Test Application
    #Initiate Application user data in DB -> should be included
    Open Browser    ${HOME PAGE}    ${BROWSER}
    
Close Test Application
    Close Browser 

Open Home Page
    Go To    ${HOME PAGE}
    Title Should Be    index page - Demo App
    Sleep    2

Click Register Link
     Click Element    xpath=//a[@href='/register']   
    
Click Login Link
     Click Element    xpath=//a[@href='/login']
         
Click Logout Link
     Click Element    xpath=//a[@href='/logout'] 

Enter UserName
     [Arguments]    ${USER NAME}
     Input Text     name=username    ${USER NAME}
     
Enter Invalid UserName
     [Arguments]   ${INVALID USERNAME} 
     Input Text    name=username    ${INVALID USERNAME}

Enter UserPassword
     [Arguments]    ${PASSWORD}
     Input Text    name=password    ${PASSWORD}

Enter Invalid UserPassword
    [Arguments]    ${INVALID USERPASSWORD}
     Input Text    name=password    ${INVALID USERPASSWORD}

Enter UserFirstName
    [Arguments]    ${FIRST NAME}
     Input Text    name=firstname    ${FIRST NAME}

Enter UserFamilyName
    [Arguments]   ${FAMILY NAME}  
     Input Text    name=lastname    ${FAMILY NAME} 

Enter UserPhoneNumber
    [Arguments]    ${PHONE} 
     Input Text    name=phone    ${PHONE} 

Click Register button
     Click Element    xpath=//input[@value='Register']

Click Login button
     Click Element    xpath=//input[@value='Log In']

Confirm Registration is Successful
      Location Should Be    ${LOGIN PAGE}

Confirm Registration is Failed
    [Arguments]    ${USER NAME}
     Location Should Be    ${REGISTER PAGE} 
     Page Should Contain    User ${USER NAME} is already registered.

Check Current User as correct
    [Arguments]    ${USER NAME} 
     Location Should Be    ${USER PAGE}
     ${CURRENT USER}    Get Text    xpath=//nav/ul/li[1]/span
     Should Be Equal    ${CURRENT USER}    ${USER NAME} 
    
Confirm User Information as correct
    [Arguments]     ${USER NAME}    ${FIRST NAME}    ${FAMILY NAME}     ${PHONE}
     Location Should Be    ${USER PAGE}     
     ${DISPLAYED USERNAME}    Get Text    xpath=//td[@id='username']
     ${DISPLAYED FIRSTNAME}    Get Text    xpath=//td[@id='firstname']
     ${DISPLAYED LASTNAME}    Get Text    xpath=//td[@id='lastname']
     ${DISPLAYED PHONE}    Get Text    xpath=//td[@id='phone']
     Should Be Equal    ${DISPLAYED USERNAME}    ${USER NAME}      
     Should Be Equal    ${DISPLAYED FIRSTNAME}    ${FIRST NAME} 
     Should Be Equal    ${DISPLAYED LASTNAME}    ${FAMILY NAME}
     Should Be Equal    ${DISPLAYED PHONE}    ${PHONE} 

Login Error Message should be displayed
     Location Should Be    ${ERROR PAGE}

    