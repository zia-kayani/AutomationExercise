
from framework.ui.locators.cart_locators import CartLocators as loc
from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page
    @property
    def cart_page_link(self):
        return loc.CART_PAGE_LINK(self.page)
    
    @property
    def first_product(self):
        return loc.FIRST_PRODUCT(self.page)
    
    @property
    def second_product(self):
        return loc.SECOND_PRODUCT(self.page)

    @property
    def continue_shopping_button(self):
        return loc.CONTINUE_SHOPPING_BUTTON(self.page)
    
    @property
    def view_cart_button(self):
        return loc.VIEW_CART_BUTTON(self.page)
    
    @property
    def first_product_name(self):
        return loc.FIRST_PRODUCT_NAME(self.page)

    @property
    def second_product_name(self):
        return loc.SECOND_PRODUCT_NAME(self.page)
    
    @property
    def add_to_cart_product(self):
        return loc.PRODUCT_ADD_TO_CART_BUTTON(self.page)
    
    @property
    def product_quantity_in_cart(self):
        return loc.PRODUCT_QUANTITY_IN_CART(self.page)

    #-----Actions ----
    def click_cart_page_link(self):
        self.cart_page_link.click()


    def add_to_cart_first_product(self):
        self.first_product.scroll_into_view_if_needed()
        self.first_product.hover()
        self.first_product.locator(
            loc.PRODUCT_OVERLAY_ADD_TO_CART_BUTTON
        ).click()

    def add_to_cart_second_product(self):
        self.second_product.scroll_into_view_if_needed()
        self.second_product.hover()
        self.second_product.locator(
            loc.PRODUCT_OVERLAY_ADD_TO_CART_BUTTON
        ).click()

    def click_continue_shopping_button(self):
        self.continue_shopping_button.click()

    def click_on_view_cart_button(self):
        self.view_cart_button.click()
    
    def check_first_product_name(self):
        expect(self.first_product_name).to_be_visible()
    
    def check_second_product_name(self):
        expect(self.second_product_name).to_be_visible()

    def click_add_to_cart_button(self):
        self.add_to_cart_product.click()

    def verify_product_quantity_in_cart(self, quantity):
        expect(self.product_quantity_in_cart).to_have_text(quantity)