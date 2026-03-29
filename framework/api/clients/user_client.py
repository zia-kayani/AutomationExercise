from framework.common.config.config import Config
import requests

API_BASE_URL = Config.API_BASE_URL
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}

class UserClient:

    #Create user client method
    def create_new_user(self, payload: dict):
        response = requests.post(f"{API_BASE_URL}/createAccount", data=payload, headers=HEADERS)
        return response
    
    #Get user details method
    def get_user_details(self, user_email:str):
        PARAMS = {"email": user_email}
        response = requests.get(f"{API_BASE_URL}/getUserDetailByEmail", params=PARAMS)
        return response
    
    #Update user 
    def update_user_details(self, payload: dict):
        response = requests.put(f"{API_BASE_URL}/updateAccount", data=payload, headers=HEADERS)
        return response
    
    #login user with valid data
    def login_user_with_valid_data(self, payload: dict):
        response = requests.post(f"{API_BASE_URL}/verifyLogin", data=payload, headers=HEADERS)
        return response
    
    #login user with invalid 
    def login_user_with_invalid_data(self, payload: dict):
        response = requests.post(f"{API_BASE_URL}/verifyLogin", data=payload, headers=HEADERS)
        return response
    
    #login user with withou email 
    def login_user_without_email(self, payload:dict):
        response = requests.post(f"{API_BASE_URL}/verifyLogin", data=payload, headers=HEADERS)
        return response

    #login user with delete method
    def login_user_with_delete_method(self):
        response = requests.delete(f"{API_BASE_URL}/verifyLogin")
        return response
    
    #test delete user method
    def delete_user(self, payload: dict):
        response = requests.delete(f"{API_BASE_URL}/deleteAccount", data=payload, headers=HEADERS)
        return response