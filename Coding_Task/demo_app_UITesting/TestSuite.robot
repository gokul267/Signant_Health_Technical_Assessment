*** Settings ***
Documentation     Test Suite with test cases for Demo App using keyword-driven testing approach
...               Test data is entered through TestData.resource file.
Library           SeleniumLibrary
Resource          Keywords.resource  
Resource          TestData.resource 
Suite Setup    Initiate Test Application     
Suite Teardown    Close Test Application

*** Test Cases ***
Test User Registration
   [Documentation]    Opens the demo app home page, clicks register link,
   ...                enters user details and verifies if the registration is successful.
   [Tags]             Positive test scenario
   Open Home Page
   Click Register Link
   Enter UserName    ${user name}
   Enter UserPassword    ${password}
   Enter UserFirstName    ${first name}
   Enter UserFamilyName    ${family name}
   Enter UserPhoneNumber    ${phone}
   Click Register button
   Confirm Registration is Successful

Validate User Information
   [Documentation]    Opens the demo app home page, clicks login link,
   ...                enters user credentials and verifies if the user information is correct.
   [Tags]             Positive test scenario
   Open Home Page
   Click Login Link
   Enter UserName    ${user name}
   Enter UserPassword    ${password}
   Click Login button
   Check Current User as correct    ${user name}
   Confirm User Information as correct    ${user name}    ${first name}    ${family name}    ${phone}
   Click Logout Link

Test Duplicate User Registration
   [Documentation]    Opens the demo app home page, clicks register link,
   ...                enters user details which is already registered in the application and 
   ...                verifies if the registration is failed.
   [Tags]             Negative test scenario
   Open Home Page
   Click Register Link
   Enter UserName    ${user name}
   Enter UserPassword    ${password}
   Enter UserFirstName    ${first name}
   Enter UserFamilyName    ${family name}
   Enter UserPhoneNumber    ${phone}
   Click Register button
   Confirm Registration is Failed    ${user name}

Test Empty Register form submit
   [Documentation]    Opens the demo app home page, clicks register link,
   ...                click register button without entering any details
   [Tags]             Negative test scenario
   Open Home Page
   Click Register Link
   Click Register button
   Location Should Be    ${REGISTER PAGE}    

Test Login with Invalid UserName
   [Documentation]    Opens the demo app home page, clicks login link,
   ...                enters user credentials with incorrect username and verifies if the login is failed.
   [Tags]             Negative test scenario
   Open Home Page
   Click Login Link
   Enter Invalid UserName    ${invalid username}
   Enter UserPassword    ${password}
   Click Login button
   Login Error Message should be displayed

Test Login with Invalid UserPassword
   [Documentation]    Opens the demo app home page, clicks login link,
   ...                enters user credentials with incorrect password and verifies if the login is failed.
   [Tags]             Negative test scenario
   Open Home Page
   Click Login Link
   Enter UserName    ${user name}
   Enter Invalid UserPassword    ${invalid userpassword}
   Click Login button
   Login Error Message should be displayed
   
Test Empty Login Form submit
   [Documentation]    Opens the demo app home page, clicks login link,
   ...                Click login button without entering user credentials
   [Tags]             Negative test scenario
   Open Home Page
   Click Login Link
   Click Login button
   Location Should Be    ${LOGIN PAGE}    


       
    