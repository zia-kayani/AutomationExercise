from framework.ui.pages.cart_page import CartPage

class CartFlow:
    def __init__(self, page):
        self.cart_page =  CartPage(page)
    

    def add_first_product_to_cart(self):
        self.cart_page.add_to_cart_first_product()

    def click_on_continue_shopping(self):
        self.cart_page.click_continue_shopping_button()

    def add_second_product_to_cart(self):
        self.cart_page.add_to_cart_second_product()
    
    def click_on_view_cart(self):
        self.cart_page.click_on_view_cart_button()
    
    def check_first_and_second_product_names(self):
        self.cart_page.check_first_product_name()
        self.cart_page.check_second_product_name()
        
     


        
        

        