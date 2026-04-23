from framework.ui.pages.auth_page import AuthPage
from framework.ui.pages.product_page import ProductPage

class ProductFlow:

    def __init__(self, page):
        self.auth_page = AuthPage(page)
        self.product_page = ProductPage(page)

    def home_page_visible(self):
        return self.auth_page.home_page_link()

    def go_to_products_page(self):
        self.product_page.click_products_page()
    
    def check_products_page_url(self):
        self.product_page.check_products_page_url()

    def click_product_view_button(self):
        self.product_page.click_product_view_button()

    def check_product_name(self):
        self.product_page.check_product_name()

    def check_product_category(self):
        self.product_page.check_product_category()
    
    def check_product_price(self):
        self.product_page.check_product_price()

    def check_product_availability(self):
        self.product_page.check_product_availability()

    def check_product_coniditon(self):
        self.product_page.check_product_coniditon()

    def check_product_brand(self):
        self.product_page.check_product_availability()

    def increase_decrease_product_quantity(self, val:str):
        self.product_page.increase_decrease_product_quantity(val)

        