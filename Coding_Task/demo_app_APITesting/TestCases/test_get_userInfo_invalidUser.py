from common.response_handler import ResponseMessage
from common.testData import *
import string

#Test get User information for given invalid user name
def test_get_userInfo_invalidUser():
    print('Get user Information API test started')

    username = inValidUser
    url = BASE_URL + '/api/users/' + username
    action = 'GET'
    request_data = ''

    getUserInfo =  ResponseMessage(url,action,request_data)
    
    assert getUserInfo.get_response_statuscode()  != 401, 'Authentication failed'
    
    assert getUserInfo.get_response_statuscode() == 404, 'Incorrect status code received'
    
    assert getUserInfo.get_status() == 'FAILURE', 'Incorrect status response received'
    
    print('Get user Information API tested successfully')
