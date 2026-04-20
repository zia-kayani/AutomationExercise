from framework.ui.locators.search_product_locator import SearchProductLocators as loc
from playwright.sync_api import expect


class SearchProductPage:
    def __init__(self, page):
        self.page = page
        

    @property 
    def product_search_input(self):
        return loc.SEARCH_INPUT(self.page)
    
    @property
    def product_search_button(self):
        return loc.SEARCH_BUTTON(self.page)
    
    @property
    def product_details_link(self):
        return loc.PRODUCT_DETAILS_LINK(self.page)
    

    #actions for the locators

    def enter_product_to_search(self, text):
        self.product_search_input.fill(text)

    def click_search_button(self):
        self.product_search_button.click()

    def check_product_details_link_visible(self):
        expect(self.product_details_link).to_be_visible()
        

