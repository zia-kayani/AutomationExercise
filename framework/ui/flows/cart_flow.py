from framework.ui.pages.cart_page import CartPage

class CartFlow:
    def __init__(self, page):
        self.cart_page =  CartPage(page)
    
    def click_on_cart_page(self):
        self.cart_page.click_cart_page_link()

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

    
    def click_add_to_cart_button(self):
        self.cart_page.click_add_to_cart_button()

    def verify_product_quantity_in_cart(self, quantity):
        self.cart_page.verify_product_quantity_in_cart(quantity)

    def remove_first_prodcut_from_cart(self):
        self.cart_page.click_to_remove_first_product_from_cart()
     
    def check_first_product_in_cart_only(self):
        self.cart_page.check_first_product_name()

    #Recommended product
    def add_to_cart_recommended_product(self):
        self.cart_page.add_to_cart_from_recommended_product()

    def check_at_least_one_product_in_cart(self):
        self.cart_page.check_at_least_one_product_in_cart()


        
    