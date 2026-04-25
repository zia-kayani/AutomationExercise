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


    #TC-13  -- Verify product quantity in cart 
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui 
    def test_verify_product_quantity_in_cart(self, page):
        
        cart_flow = CartFlow(page)
        auth_flow = AuthFlow(page)
        product_flow =  ProductFlow(page)

        assert auth_flow.home_page_visible(), "Home Page is not visible "
        product_flow.go_to_products_page()
        product_flow.click_product_view_button()
        product_flow.check_product_name(), "Product details are not there "
        product_flow.increase_decrease_product_quantity("4")    
        cart_flow.click_add_to_cart_button()
        cart_flow.click_on_view_cart()  
        cart_flow.verify_product_quantity_in_cart("4")  
        


    #TC-17  -- Remove product from  cart 
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui 
    def test_remove_product_from_cart(self, page):
        
        cart_flow = CartFlow(page)
        auth_flow = AuthFlow(page)
        product_flow =  ProductFlow(page)

        assert auth_flow.home_page_visible(), "Home Page is not visible "
        product_flow.go_to_products_page()
        cart_flow.add_first_product_to_cart()
        cart_flow.click_on_view_cart()

        cart_flow.remove_first_prodcut_from_cart(), "Product is not removed "

    #TC-22  Add to cart from Recommended product
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui 
    @pytest.mark.only
    def test_add_to_cart_recommended_products(self, page):
        
        cart_flow = CartFlow(page)
        auth_flow = AuthFlow(page)
        product_flow =  ProductFlow(page)

        assert auth_flow.home_page_visible(), "Home Page is not visible "
        product_flow.recommended_products_heading_check()

        cart_flow.add_to_cart_recommended_product()

        cart_flow.click_on_view_cart()

        cart_flow.check_at_least_one_product_in_cart()

