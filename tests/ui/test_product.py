from framework.ui.flows.product_flow import ProductFlow
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

        



