from framework.common.config.config import Config
import requests

API_BASE_URL = Config.API_BASE_URL
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}

class UserClient:
    def create_new_user(self, payload: dict):
        response = requests.post(f"{API_BASE_URL}/createAccount", data=payload, headers=HEADERS)
        return response