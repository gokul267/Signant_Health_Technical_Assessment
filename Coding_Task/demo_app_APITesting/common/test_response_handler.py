import unittest
import jsonpath
import json
from .response_handler import ResponseMessage

dummy =  ResponseMessage('http://localhost:8080/api/users','GET','')

sample_response = """{
                    "message": "retrieval succesful",
                    "payload": {
                        "firstname": "value1",
                        "lastname": "value2",
                        "phone": "value3"
                    },
                    "status": "SUCCESS"
                    }"""
                    
content = json.loads(sample_response)
dummy.status_code = 200  
dummy.status = jsonpath.jsonpath(content, 'status')
dummy.payload = jsonpath.jsonpath(content, 'payload')
dummy.message = jsonpath.jsonpath(content, 'message')

class TestResponseMessage(unittest.TestCase):
    
    def test_get_response_statuscode(self):
        self.assertEqual(dummy.get_response_statuscode(), 200)
    
    def test_get_message(self):
        self.assertEqual(dummy.get_message(), 'retrieval succesful')
            
    def test_get_status(self):
        self.assertEqual(dummy.get_status(), 'SUCCESS') 
    
    def test_get_payload(self):
        self.assertEqual(dummy.get_payload(), {'firstname': 'value1', 'lastname': 'value2', 'phone': 'value3'})
            
    def test_get_first_name(self):
        self.assertEqual(dummy.get_first_name(), 'value1')
    
    def test_get_last_name(self):
        self.assertEqual(dummy.get_last_name(), 'value2')
    
    def test_get_phone(self):
        self.assertEqual(dummy.get_phone(), 'value3')