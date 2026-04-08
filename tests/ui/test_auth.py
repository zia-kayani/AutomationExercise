# tests/ui/test_auth.py

from framework.ui.flows.auth_flow import AuthFlow
import pytest


# -------------------------------Test Class for User Registration-------------------------------------
class TestRegistration:

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


#-------------------------------Test Class for User Login-------------------------------------
class TestLoginn:

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