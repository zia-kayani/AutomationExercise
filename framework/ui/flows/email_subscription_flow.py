from framework.ui.pages.email_subscription_page import EmailSubscriptionPage


class EmmailSubscriptionFlow :

    def __init__(self, page):
       self.email_subscription_page =  EmailSubscriptionPage(page)

    def enter_email_and_get_subscribed(self, email):
        self.email_subscription_page.scroll_to_footer()
        self.email_subscription_page.verify_subscription_text_visible()
        self.email_subscription_page.type_email_address(email)
        self.email_subscription_page.click_on_subscribe_button()
        self.email_subscription_page.check_subscribe_success_message()


    #cart page method flow
    def click_on_cart_page(self):
        self.email_subscription_page.click_cart_page_link()