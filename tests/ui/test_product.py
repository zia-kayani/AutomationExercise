from framework.ui.flows.product_flow import ProductFlow
from framework.ui.flows.auth_flow import AuthFlow
import pytest

class TestProductClass:

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_product(self,page):
        flow =  ProductFlow(page)

        assert flow.home_page_visible(), "Home page is not visible"

        flow.go_to_products_page()
        flow.check_products_page_url()
        flow.click_product_view_button()

        flow.check_product_name(), "product name is not visible "
        flow.check_product_category(), "product category is not visible "
        flow.check_product_price(), "product price is not visible "
        flow.check_product_availability(), "product availability is not visible "
        flow.check_product_coniditon(), "product condition is not visible "
        flow.check_product_brand(), "product brand is not visible "


    #TC-21  Add Review on Product 
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.regression 
    @pytest.mark.only
    @pytest.mark.parametrize("name, email, message", [("zia", "zia@gmail.com", "product is very nice and good quality")])
    def test_give_product_review(self, page, name, email, message):
        auth_flow = AuthFlow(page)
        product_flow = ProductFlow(page)

        auth_flow.home_page_visible(), "Home page is not visible "
        
        product_flow.go_to_products_page()
        product_flow.click_product_view_button()
        product_flow.submit_product_review_form(name , email, message)

        
        



