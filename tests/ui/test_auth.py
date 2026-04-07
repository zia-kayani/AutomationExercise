# tests/ui/test_auth.py

from framework.ui.flows.auth_flow import AuthFlow

def test_user_registration(page, user_data):
    flow = AuthFlow(page)

    flow.register_new_user(user_data)

    assert flow.verify_account_created(), "Account was not created"
    flow.continue_after_signup()
    assert flow.auth_page.logout_link.is_visible(), "Logout link not visible, registration might have failed"
    assert flow.auth_page.delete_account_link.is_visible(), "Delete Account link not visible, registration might have failed"

    flow.delete_account()

    # flow.logout()
