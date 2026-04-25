from framework.ui.flows.search_product_flow import SearchProductFlow
from framework.ui.flows.product_flow import ProductFlow
from framework.ui.flows.cart_flow import CartFlow
from framework.ui.flows.auth_flow import AuthFlow
import time


import pytest

class TestSearchProduct:

    # Test Case 20: Search Products and Verify Cart After Login
    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.parametrize("prod", ["Blue Top"])
    def test_search_product(self, page, prod, user_data, registered_user):

        product_flow =  ProductFlow(page)
        search_product_flow =  SearchProductFlow(page)
        cart_flow  =  CartFlow(page)
        auth_flow = AuthFlow(page)

        product_flow.home_page_visible()
        product_flow.go_to_products_page() 
        product_flow.check_products_page_url() ,"User is not on products page "

        search_product_flow.type_product_name_and_click_search(prod)

        product_flow.click_product_view_button()
        cart_flow.click_add_to_cart_button()
        cart_flow.click_on_view_cart() 
        auth_flow.register_new_user(user_data)
        auth_flow.continue_after_signup()
        auth_flow.logout_user()


        auth_flow.login_with_credentials(
            user_data["email"],
            user_data["password"]
        ), "Login failed"
        cart_flow.click_on_cart_page()
        cart_flow.check_first_product_in_cart_only() , "Product is not the cart "





