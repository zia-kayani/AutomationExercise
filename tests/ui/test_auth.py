# tests/ui/test_auth.py

from framework.ui.flows.auth_flow import AuthFlow
import pytest


# -------------------------------Test Class for User Registration-------------------------------------
class TestRegistration:

    #TC: Verify that a new user can register successfully
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    def test_user_registration(self,page, user_data):
        flow = AuthFlow(page)

        flow.register_new_user(user_data)

        assert flow.verify_account_created(), "Account was not created"
        flow.continue_after_signup()
        assert flow.auth_page.logout_link.is_visible(), "Logout link not visible, registration might have failed"
        assert flow.auth_page.delete_account_link.is_visible(), "Delete Account link not visible, registration might have failed"

        # flow.delete_account()

        # flow.logout()


    #TC: Verify that user cannot register with existing email
    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.only

    def test_registeration_with_existing_email(self, page,user_data):
        flow = AuthFlow(page)

        assert flow.home_page_visible(), "Home page is not visible"
        flow.register_with_existing_email(user_data)

        assert flow.verify_email_already_exists_message(), "Email already exists text not visible, validation might have failed"






#-------------------------------Test Class for User Login-------------------------------------
class TestLogin:

    #TC: Verify that a registered user can login successfully
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    def test_user_login(self, page, registered_user):
        flow = AuthFlow(page)

        
        assert flow.home_page_visible(), "Home page is not visible"
        flow.login_with_credentials(registered_user["email"], registered_user["password"])
        assert flow.auth_page.logged_in_as.is_visible(), "Logged in as text not visible, login might have failed"
        flow.delete_account_after_login()
        assert flow.verify_account_deleted(), "Account was not deleted"



    #TC: Verify that user cannot login with invalid credentials
    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.parametrize("email,password", [("test@example.com", "wrongpassword")])
    def test_login_with_invalid_credentials(self, page, email, password):
        flow = AuthFlow(page)

        assert flow.home_page_visible(), "Home page is not visible"
        flow.login_with_credentials(email, password)

        assert flow.verify_incorrect_email_password_message(), "Incorrect email/password text not visible, validation might have failed"



    #TC: Verify logout user successfully
    @pytest.mark.regression
    @pytest.mark.ui

    def test_user_logout(self, page, user_data):
        flow = AuthFlow(page)

        assert flow.home_page_visible(), "Home page is not visible"
        flow.login_with_credentials(user_data["email"], user_data["password"])
        # flow.login_with_credentials(email, password)

        assert flow.auth_page.logged_in_as.is_visible(), "Logged in as text not visible, login might have failed"
        flow.logout_user()
        assert flow.login_heading_visible(), "Login heading not visible after logout, logout might have failed"


    


