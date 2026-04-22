import pytest
from framework.ui.flows.auth_flow import AuthFlow
from framework.ui.flows.checkout_flow import CheckoutFlow
from framework.ui.flows.product_flow import ProductFlow
from framework.ui.flows.cart_flow import CartFlow

class TestCheckout:

    #TC-14 -- Place Order: Register while Checkout
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.parametrize(
        "comment, name, card, cvc, month, year",
        [
            (
                "Please deliver fast",
                "Test User",
                "4111111111111111",
                "123",
                "12",
                "2030"
            )
        ]
    )
    def test_place_order_and_verify_success(self, page,comment,name,card,cvc,month,year, user_data
    ):

        auth_flow = AuthFlow(page)
        checkout_flow = CheckoutFlow(page)
        product_flow = ProductFlow(page)
        cart_flow = CartFlow(page)

        assert auth_flow.home_page_visible(), "Home page is not visible"
        product_flow.go_to_products_page()
        product_flow.click_product_view_button()
        cart_flow.click_add_to_cart_button()
        cart_flow.click_on_view_cart()  


        # FULL CHECKOUT FLOW
        checkout_flow.proceed_to_checkout_from_cart()
        checkout_flow.register_or_login_from_checkout()
        auth_flow.register_new_user(user_data)  
        auth_flow.verify_account_created() , "Account was not created"
        auth_flow.continue_after_signup()
        auth_flow.verify_logged_in() , "Account is not logged in "

        cart_flow.click_on_cart_page()
        
        checkout_flow.proceed_to_checkout_from_cart()

        checkout_flow.verify_address_details()
        checkout_flow.add_order_comment(comment)
        checkout_flow.proceed_to_place_order()

        checkout_flow.enter_payment_details(
            name, card, cvc, month, year
        )
        checkout_flow.confirm_payment()

        # ASSERT ORDER SUCCESS
        checkout_flow.checkout_page.verify_order_success()





    #TC-15 -- Place Order: Register before Checkout
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.parametrize(
        "comment, name, card, cvc, month, year",
        [
            (
                "Please deliver fast",
                "Test User",
                "4111111111111111",
                "123",
                "12",
                "2030"
            )
        ]
    )
    def test_resiter_and_login_and_place_order_and_verify_success(self, page,comment,name,card,cvc,month,year, user_data
    ):

        auth_flow = AuthFlow(page)
        checkout_flow = CheckoutFlow(page)
        product_flow = ProductFlow(page)
        cart_flow = CartFlow(page)

        assert auth_flow.home_page_visible(), "Home page is not visible"

        auth_flow.register_new_user(user_data)  
        auth_flow.verify_account_created() , "Account was not created"
        auth_flow.continue_after_signup()
        auth_flow.verify_logged_in() , "Account is not logged in "


        product_flow.go_to_products_page()
        product_flow.click_product_view_button()
        cart_flow.click_add_to_cart_button()
        cart_flow.click_on_view_cart()  

        checkout_flow.proceed_to_checkout_from_cart()


        checkout_flow.verify_address_details()
        checkout_flow.add_order_comment(comment)
        checkout_flow.proceed_to_place_order()

        checkout_flow.enter_payment_details( name, card, cvc, month, year)
        checkout_flow.confirm_payment()

        checkout_flow.checkout_page.verify_order_success()

    