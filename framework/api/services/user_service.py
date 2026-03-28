from framework.api.clients.user_client import UserClient

class UserService:
    def __init__(self):
        self.user_client = UserClient()

    def create_new_user(self, payload: dict):
        response = self.user_client.create_new_user(payload)
        data = response.json()

        if data.get("responseCode") != 201:
            raise Exception(f"Failed to create user. Response: {data}")

        return data