from framework.api.clients.user_client import UserClient

class UserService:
    def __init__(self):
        self.user_client = UserClient()

    #Create user service method
    def create_new_user(self, payload: dict):
        response = self.user_client.create_new_user(payload)
        data = response.json()

        if data.get("responseCode") != 201:
            raise Exception(f"Failed to create user. Response: {data}")

        return data
    
    #get user details service method
    def get_user_details(self, payload: str):
        response = self.user_client.get_user_details(payload)
        data =  response.json()

        if data.get("responseCode") != 200:
            raise Exception(f"Failed to create user. Response: {data}")
        return data
    
    
    #update user details service method
    def update_user_details(self, payload: dict):
        response = self.user_client.update_user_details(payload)
        data = response.json()

        if data.get("responseCode") != 200:
            raise Exception(f"Failed to update user. Response: {data}")
        return data

    #login user with valid data service method
    def login_user_with_valid_data(self, payload:dict):
        respoonse =  self.user_client.login_user_with_valid_data(payload)
        data = respoonse.json()
        if data.get("responseCode") != 200:
            raise Exception(f"Failed to login user. Response: {data}")
        return data
    
    #login user with invalid data service method
    def login_user_with_invalid_data(self, payload:dict):
        response = self.user_client.login_user_with_invalid_data(payload)
        data = response.json()
        if data.get("responseCode") != 404:
            raise Exception(f"Expected login failure with invalid data. Response: {data}")
        return data

    #login user without email service method
    def login_user_without_email(self, payload:dict):
        response = self.user_client.login_user_without_email(payload)
        data = response.json()
        if data.get("responseCode") != 400:
            raise Exception(f"Expected login failure without email. Response: {data}")
        return data

    #login user with delete method service method
    def login_user_with_delete_method(self):
        response = self.user_client.login_user_with_delete_method()
        data = response.json()
        if data.get("responseCode") != 405:
            raise Exception(f"Expected method not allowed for delete login. Response: {data}")
        return data

    #delete user service method 
    def delete_user_service(self, payload: dict):
        response = self.user_client.delete_user(payload)
        data = response.json()
        if data.get("responseCode") != 200:
            raise Exception(f"Failed to delete user. Response: {data}")
        return data
    
    
    