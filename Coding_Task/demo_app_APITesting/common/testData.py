BASE_URL = "http://localhost:8080"
TOKEN = 'MTkyMjk4MTQ1OTU5NTkwMDczMzI1MTg3MjI4OTcxNDQyOTI4MjI1'

#User who is successfully registered
validUser = 'Gokul'
inValidUser = 'Random'

#Values already configured for the user mentioned above as validUser
validFirstName = 'Gokul'
validLastName = 'Gokul'
validPhone = 'Gokul'


#Values updated for the user mentioned above as validUser
updateUserData1 = """{
                        "firstname": "value1",
                        "lastname": "value2",
                        "phone": "value3"
                }"""

#Test to update user info with empty values for user mentioned above as validUser
updateUserData2 = """{
                        "firstname": "",
                        "lastname": "",
                        "phone": ""
                }"""

#Test to update user info with empty keys for user mentioned above as validUser
updateUserData3 = """{
                        "": "value3"
                }"""
                
#Test to update user info with empty keys for user mentioned above as validUser
updateUserData4 = """{}"""
