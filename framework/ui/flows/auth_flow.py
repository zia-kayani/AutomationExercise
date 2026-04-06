# framework/ui/flows/auth_flow.py

from framework.ui.pages.auth_page import AuthPage


class AuthFlow:

    def __init__(self, page):
        self.auth_page = AuthPage(page)

    def register_new_user(self, user_data: dict):
        """
        Full end-to-end registration flow
        """

        self.auth_page.go_to_signup_login()

        self.auth_page.signup(
            user_data["name"],
            user_data["email"]
        )

        self.auth_page.fill_account_info(
            user_data["password"],
            user_data["day"],
            user_data["month"],
            user_data["year"]
        )

        self.auth_page.fill_address_info(
            user_data["first_name"],
            user_data["last_name"],
            user_data["company"],
            user_data["address"],
            user_data["address2"],
            user_data["country"],
            user_data["state"],
            user_data["city"],
            user_data["zipcode"],
            user_data["mobile"]
        )

        self.auth_page.create_account()

    def verify_account_created(self):
        return self.auth_page.account_created_text.is_visible()

    def continue_after_signup(self):
        self.auth_page.continue_after_registration()


    def delete_account(self):
        self.auth_page.delete_account()
    
    def logout(self):
        self.auth_page.logout()