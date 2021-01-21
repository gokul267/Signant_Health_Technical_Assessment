from common.response_handler import ResponseMessage
from common.testData import *

#Test get User information for given user name
def test_get_userInfo_validUser():
    print('Get user Information API test started')
    
    username = validUser
    url = BASE_URL + '/api/users/' + username
    action = 'GET'
    request_data = ''
    
    getUserInfo =  ResponseMessage(url,action,request_data)
    
    assert getUserInfo.get_response_statuscode()  != 401, 'Authentication failed'
    
    assert getUserInfo.get_response_statuscode() == 200, 'API call failed'
    
    assert getUserInfo.get_status() == 'SUCCESS', 'Message request failed'
    
    firstname = getUserInfo.get_first_name()
    
    assert firstname == validFirstName, 'Validation failed for firstname : Expected = ' + validFirstName +', found = ' + firstname
    
    lastname = getUserInfo.get_last_name()
    
    assert lastname == validLastName, 'Validation failed for lastname : Expected = ' + validLastName +', found = ' + lastname
    
    phone = getUserInfo.get_phone()
    
    assert phone == validPhone, 'Validation failed for phone : Expected = ' + validPhone +', found = ' + phone
    
    print('Get user Information API tested successfully')