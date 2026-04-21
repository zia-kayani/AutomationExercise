from playwright.sync_api import expect   

from framework.ui.locators.email_subscription_locators import EmailSubscriptionLocators as loc


class EmailSubscriptionPage:

    def __init__(self, page):
        self.page = page
    @property
    def footer(self):
        return loc.FOOTER(self.page)
    
    @property
    def subscription_text(self):
        return loc.SUBSCRIPTION_TEXT(self.page)

    @property
    def subscribe_email_input(self):
        return loc.SUBSCRIBE_EMAIL_INPUT(self.page)
    
    @property
    def subscribe_email_button(self):
        return loc.SUBSCRIBE_EMAIL_BUTTON(self.page) 
    
    @property
    def subscribe_success_message(self):
        return loc.SUBSCRIBE_SUCCESS_MESSAGE(self.page)
    
    #cart page email subscription property
    @property
    def cart_page_link(self):
        return loc.CART_PAGE_LINK(self.page)

    # --actions

    def scroll_to_footer(self):
        self.footer.scroll_into_view_if_needed()
        expect(self.footer).to_be_visible()

    def verify_subscription_text_visible(self):
        expect(self.subscription_text).to_be_visible()


    def type_email_address(self, text:str):
        expect(self.subscribe_email_input).to_be_visible()
        self.subscribe_email_input.fill(text)

    def click_on_subscribe_button(self):
        self.subscribe_email_button.click()

    def check_subscribe_success_message(self):
        expect(self.subscribe_success_message).to_be_visible()


    #action for cart page 
    def click_cart_page_link(self):
        self.cart_page_link.click()

