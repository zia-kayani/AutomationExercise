from framework.ui.locators.checkout_locators import CheckoutLocators as loc
from playwright.sync_api import expect


class CheckoutPage:
    def __init__(self, page):
        self.page = page


    @property
    def proceed_to_checkout_button(self):
        return loc.PROCEED_TO_CHECKOUT_BUTTON(self.page)

    @property
    def register_login_link(self):
        return loc.CHECKOUT_REGISTER_LOGIN_LINK(self.page)

    @property
    def address_details_heading(self):
        return loc.ADDRESS_DETAILS_HEADING(self.page)

    @property
    def comment_textarea(self):
        return loc.COMMENT_TEXT_AREAD_INPUT(self.page)

    @property
    def place_order_button(self):
        return loc.PLACE_ORDER_BUTTON(self.page)

    @property
    def name_on_card(self):
        return loc.NAME_ON_CARD(self.page)

    @property
    def card_number(self):
        return loc.CARD_NUMBER(self.page)

    @property
    def cvc(self):
        return loc.CVC(self.page)

    @property
    def expiry_month(self):
        return loc.EXPIRY_MONTH(self.page)

    @property
    def expiry_year(self):
        return loc.EXPIRY_YEAR(self.page)

    @property
    def pay_and_confirm_button(self):
        return loc.PAY_AND_CONFRIM_BUTTON(self.page)

    @property
    def order_confirmation_message(self):
        return loc.ORDER_CONFIRMATION_MESSAGE(self.page)
    
    @property
    def checkout_page_address_detail(self):
        return loc.CHECKPUT_PAGE_ADDRESS(self.page)
    
    @property
    def download_invoice_button(self):
        return loc.DOWNLOAD_INVOICE_BUTTON_AFTER_DOWNLOAD(self.page)

    # ACTIONS

    def click_proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()

    def click_register_login(self):
        self.register_login_link.click()

    def verify_address_details_visible(self):
        expect(self.address_details_heading).to_be_visible()

    def add_comment(self, message: str):
        self.comment_textarea.fill(message)

    def click_place_order(self):
        self.place_order_button.click()

    def fill_card_details(self, name, number, cvc, month, year):
        self.name_on_card.fill(name)
        self.card_number.fill(number)
        self.cvc.fill(cvc)
        self.expiry_month.fill(month)
        self.expiry_year.fill(year)

    def click_pay_and_confirm(self):
        self.pay_and_confirm_button.click()

    def verify_order_success(self):
        expect(self.order_confirmation_message).to_be_visible()

    def checkout_page_address(self, expected_address):
        expect(self.checkout_page_address_detail).to_contain_text(expected_address)

    def click_download_invoice_button(self):
        self.download_invoice_button.click()