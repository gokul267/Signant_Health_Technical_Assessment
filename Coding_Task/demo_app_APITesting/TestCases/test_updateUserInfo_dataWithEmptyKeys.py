import json
from common.response_handler import ResponseMessage
from common.testData import *

#Test update user information for given user name with empty keys
def test_put_userInfo_emptyKeys():
    print('Update user Information API test started')
    
    username = validUser
    url = BASE_URL + '/api/users/' + username
    action = 'PUT'
    
    request_data = json.loads(updateUserData3);
    
    updateUserInfo = ResponseMessage(url,action,request_data)
    
    assert updateUserInfo.get_response_statuscode()  != 401, 'Authentication failed'
    
    assert updateUserInfo.get_response_statuscode() == 403, 'Incorrect HTTP status code received'
    
    assert updateUserInfo.get_message() == 'Field update not allowed', 'Incorrect response message received'
    
    assert updateUserInfo.get_status() == 'FAILURE', 'Incorrect status response received'
    
    print('Update user information API tested successfully')