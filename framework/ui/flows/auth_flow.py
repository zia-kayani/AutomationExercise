# framework/ui/flows/auth_flow.py

from framework.ui.pages.auth_page import AuthPage


class AuthFlow:

    def __init__(self, page):
        self.auth_page = AuthPage(page)
    # --------------------------------------User Registration Flow-------------------------------------

    # Full end-to-end registration flow
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

    # Register user with existing email 
    def register_with_existing_email(self, user_data):
        self.auth_page.go_to_signup_login()

        self.auth_page.signup(
            user_data["name"],
            user_data["email"]
        )
    
    def verify_email_already_exists_message(self):
        return self.auth_page.email_already_exists_text_visible()

    # --------------------------------------User Login Flow-------------------------------------
    def home_page_visible(self):
        return self.auth_page.home_page_link()
    
    def login_with_credentials(self, email, password):
        self.auth_page.go_to_signup_login()
        self.auth_page.login_heading_visible()
        self.auth_page.enter_login_email(email)
        self.auth_page.enter_login_password(password)
        self.auth_page.click_login_button()
    
    def verify_logged_in(self):
        return self.auth_page.logged_in_as_visible()
    
    def delete_account_after_login(self):
        self.auth_page.delete_account_after_login()
    
    def verify_account_deleted(self):
        return self.auth_page.account_deleted_text_visible()
    

    #login with invalid credentials error message visible
    def verify_incorrect_email_password_message(self):
        return self.auth_page.incorrect_email_password_text_visible()
    
    #logout user successfully
    def logout_user(self):
        self.auth_page.click_logout()

    def login_heading_visible(self):
        return self.auth_page.login_heading_visible()
    
