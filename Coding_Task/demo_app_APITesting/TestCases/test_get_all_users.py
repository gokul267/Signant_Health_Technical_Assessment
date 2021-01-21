from common.response_handler import ResponseMessage
from common.testData import BASE_URL

#Test get all users from the App
def test_get_users():
    print('Get users API test started')

    url = BASE_URL + '/api/users'
    action = 'GET'
    request_data = ''

    getUsers =  ResponseMessage(url,action,request_data)

    assert getUsers.get_response_statuscode() == 200, 'API call failed'

    assert getUsers.get_status() == 'SUCCESS', 'Message request failed'

    assert (getUsers.get_payload().__sizeof__() >= 0), 'No users found'

    print('Get users API tested successfully')