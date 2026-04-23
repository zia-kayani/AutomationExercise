import pytest
from framework.ui.flows.brands_flow import BrandsFlow
from framework.ui.flows.product_flow import ProductFlow
from framework.ui.flows.auth_flow import AuthFlow


class TestBrands:

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    def test_verify_polo_brand_products(self, page):

        auth_flow = AuthFlow(page)
        product_flow = ProductFlow(page)
        brands_flow = BrandsFlow(page)

        assert auth_flow.home_page_visible(), "Home page not visible"

        product_flow.go_to_products_page()

        brands_flow.open_polo_brand_and_verify()

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    def test_verify_hm_brand_products(self, page):

        auth_flow = AuthFlow(page)
        product_flow = ProductFlow(page)
        brands_flow = BrandsFlow(page)

        assert auth_flow.home_page_visible(), "Home page not visible"

        product_flow.go_to_products_page()

        brands_flow.open_hm_brand_and_verify()