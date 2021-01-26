import json
from common.response_handler import ResponseMessage
from common.testData import *

#Test update user information for given user name for an invalid user
def test_put_userInfo_InvalidUser_completeData():
    print('Update user Information API test started')
    
    username = validUser
    url = BASE_URL + '/api/users/' + inValidUser
    action = 'PUT'
    
    request_data = json.loads(updateUserData1);
    updatedFirstName = request_data['firstname']
    updatedLastName = request_data['lastname']
    updatedPhone = request_data['phone']
    
    updateUserInfo = ResponseMessage(url,action,request_data)
    
    assert updateUserInfo.get_response_statuscode()  != 401, 'Authentication failed'
    
    assert updateUserInfo.get_response_statuscode() == 403, 'API call failed'
    
    assert updateUserInfo.get_message() == 'Updated', 'Message update failed'
    
    assert updateUserInfo.get_status() == 'SUCCESS', 'Message update failed'
    
    #Validate if the data is updated correctly
    url = BASE_URL + '/api/users/' + username
    action = 'GET'
    request_data = ''
    
    updateUserInfo = ResponseMessage(url,action,request_data)
    
    assert updateUserInfo.get_response_statuscode() == 200, 'API call failed'
    
    firstname = updateUserInfo.get_first_name()
    
    assert firstname == updatedFirstName, 'Validation failed for firstname : Expected = ' + updatedFirstName +', found = ' + firstname
    
    lastname = updateUserInfo.get_last_name()
    
    assert lastname == updatedLastName, 'Validation failed for lastname : Expected = ' + updatedLastName +', found = ' + lastname
    
    phone = updateUserInfo.get_phone()
    
    assert phone == updatedPhone, 'Validation failed for phone : Expected = ' + updatedPhone +', found = ' + phone
    
    print('Update user information API tested successfully')