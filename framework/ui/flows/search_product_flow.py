from framework.ui.pages.search_product_page import SearchProductPage

class SearchProductFlow:

    def __init__(self, page):
        self.search_product_page =  SearchProductPage(page)

    def type_product_name_and_click_search(self, prod:str):
        self.search_product_page.enter_product_to_search(prod)
        self.search_product_page.click_search_button()
        self.search_product_page.check_product_details_link_visible()
            

            