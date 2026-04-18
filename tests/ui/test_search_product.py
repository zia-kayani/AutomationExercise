from framework.ui.flows.search_product_flow import SearchProductFlow
from framework.ui.flows.product_flow import ProductFlow

import pytest

class TestSearchProduct:
    @pytest.mark.regression
    @pytest.mark.smoke

    def test_search_product(self, page, prod="Men Tshirt"):

        product_flow =  ProductFlow(page)
        search_product_flow =  SearchProductFlow(page)

        product_flow.home_page_visible()
        product_flow.go_to_products_page() 

        search_product_flow.type_product_name_and_click_search(prod)
    

       
