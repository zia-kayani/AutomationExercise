from framework.ui.flows.cart_flow import CartFlow
from framework.ui.flows.auth_flow import AuthFlow
from framework.ui.flows.product_flow import ProductFlow

import pytest

class TestCart:
    #TC - Add first and second product to cart and view the cart 
    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ui 
    def test_add_to_cart_first_and_second_product_and_verify(self,page):
        cart_flow = CartFlow(page)
        auth_flow = AuthFlow(page)
        product_flow =  ProductFlow(page)

        assert auth_flow.home_page_visible(), "Home Page is not visible "
        product_flow.go_to_products_page()
        cart_flow.add_first_product_to_cart()
        cart_flow.click_on_continue_shopping()
        cart_flow.add_second_product_to_cart()
        cart_flow.click_on_view_cart()

        cart_flow.check_first_and_second_product_names(), "First and second product names are not visible"
        