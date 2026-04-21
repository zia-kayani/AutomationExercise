from framework.ui.flows.email_subscription_flow import EmmailSubscriptionFlow
from framework.ui.flows.auth_flow import AuthFlow

import pytest

class TestEmailSubscription :

    #TC -  Subscribe EMail for future updates on home page
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    def test_email_subscription(self, page, user_email):
        auth_flow = AuthFlow(page)
        email_subscription_flow =  EmmailSubscriptionFlow(page)
        auth_flow.home_page_visible()
        email_subscription_flow.enter_email_and_get_subscribed(user_email)

    
    #TC - subscribe email on cart page 
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    def test_email_subscription_on_cart_page(self, page, user_email):
        auth_flow = AuthFlow(page)
        email_subscription_flow =  EmmailSubscriptionFlow(page)
        auth_flow.home_page_visible()
        email_subscription_flow.click_on_cart_page()
        email_subscription_flow.enter_email_and_get_subscribed(user_email)

