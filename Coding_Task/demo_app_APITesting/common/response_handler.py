import requests
import json
import jsonpath
from .testData import TOKEN

headers = {'Content-Type':'application/json', 'Token': ''+TOKEN+''}

class ResponseMessage:

    def __init__(self,url,action,request_data):
        
        print("URL invoked : " + url + ", Action : " + action + ", request_data : " + json.dumps(request_data))
        
        if action=='GET': 
            response  = requests.get(url, headers=headers)
        elif action=='PUT':
            response  = requests.put(url, data=json.dumps(request_data) ,headers=headers)
        else:
            raise 'Incorrect HTTP action used'
        
        print("response status code : " + str(response.status_code))
        
        if response.status_code != 500 :             
            print("response text : " +response.text)               
            self.statuscode =  response.status_code
            self.content = json.loads(response.text)    
            self.status = jsonpath.jsonpath(self.content, 'status')
            self.payload = jsonpath.jsonpath(self.content, 'payload')
            self.message = jsonpath.jsonpath(self.content, 'message')
        else:
            self.statuscode =  response.status_code
         
    #def get_content(self):
        #return self.content
    
    def get_response_statuscode(self):
        return self.statuscode
    
    def get_message(self):
        return  self.message[0]
    
    def get_status(self):
        return  self.status[0]
    
    def get_payload(self):
        return  self.payload[0]
    
    def get_first_name(self):
        return jsonpath.jsonpath(self.payload[0],'firstname')[0]
    
    def get_last_name(self):
        return jsonpath.jsonpath(self.payload[0],'lastname')[0]
    
    def get_phone(self):
        return jsonpath.jsonpath(self.payload[0],'phone')[0]