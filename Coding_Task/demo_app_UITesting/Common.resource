*** Settings ***
Documentation     Project common resource file with test keywords and variables
Library           SeleniumLibrary      

*** Variables ***
${BROWSER}        chrome
${HOST}           localhost:8080
${HOME PAGE}      http://${HOST}/
${LOGIN PAGE}      http://${HOST}/login
${REGISTER PAGE}      http://${HOST}/register
${USER PAGE}      http://${HOST}/user
${ERROR PAGE}      http://${HOST}/error
