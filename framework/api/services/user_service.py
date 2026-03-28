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

    


    
    