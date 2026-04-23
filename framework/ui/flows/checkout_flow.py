from framework.ui.pages.checkout_page import CheckoutPage


class CheckoutFlow:

    def __init__(self, page):
        self.checkout_page = CheckoutPage(page)

    # CART → CHECKOUT FLOW

    def proceed_to_checkout_from_cart(self):
        self.checkout_page.click_proceed_to_checkout()

    def register_or_login_from_checkout(self):
        self.checkout_page.click_register_login()

    # ADDRESS SECTION FLOW

    def verify_address_details(self):
        self.checkout_page.verify_address_details_visible()

    def add_order_comment(self, comment: str):
        self.checkout_page.add_comment(comment)

    def proceed_to_place_order(self):
        self.checkout_page.click_place_order()

    # PAYMENT FLOW

    def enter_payment_details(self, name, card_number, cvc, month, year):
        self.checkout_page.fill_card_details(
            name,
            card_number,
            cvc,
            month,
            year
        )

    def confirm_payment(self):
        self.checkout_page.click_pay_and_confirm()

    # COMPLETE END-TO-END FLOW

    def complete_order(self, comment, name, card, cvc, month, year):
        self.checkout_page.click_proceed_to_checkout()
        self.checkout_page.verify_address_details_visible()

        self.checkout_page.add_comment(comment)
        self.checkout_page.click_place_order()

        self.checkout_page.fill_card_details(name, card, cvc, month, year)
        self.checkout_page.click_pay_and_confirm()

        self.checkout_page.verify_order_success()