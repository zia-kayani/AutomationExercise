from framework.ui.locators.products_locators import ProductsLocators as loc
from playwright.sync_api import expect



class ProductPage:

    def __init__(self, page):
        self.page =  page

    
    @property
    def  products_page_link(self):
        return loc.PRODUCTS_PAGE_LINK(self.page)
    
    @property
    def products_page_url(self):
        return loc.PRODUCTS_PAGE_URL
    
    @property
    def featured_products_list(self):
        return loc.FEATURED_PRODUCTS_LIST(self.page)
    
    @property
    def first_product_view_product_button(self):
        return loc.FIRST_PRODUCT_VIEW_PRODUCT_BUTTON(self.page)
    
    @property
    def product_name(self):
        return loc.PRODUCT_NAME(self.page)
     
    @property
    def product_category(self):
        return loc.PRODUCT_CATEGORY(self.page)   
    
    @property
    def product_price(self):
        return loc.PRODUCT_PRICE(self.page)
    
    
    @property
    def product_availability(self):
        return loc.PRODUCT_AVAILABILITY(self.page)
    
    
    @property
    def product_condition(self):
        return loc.PRODUCT_CATEGORY(self.page)
    
    @property
    def product_brand(self):
        return loc.PRODUCT_BRAND(self.page)  
    

    #----actions ---

    def click_products_page(self):
        self.products_page_link.click()

    def check_products_page_url(self):
        expect(self.page).to_have_url(self.products_page_url)


    def check_featured_products_list(self):
        expect(self.featured_products_list).is_visible()

    def click_product_view_button(self):
        self.first_product_view_product_button.click()


    def check_product_name(self):
        expect(self.product_name).to_be_visible()

    def check_product_category(self):
        expect(self.product_category).to_be_visible()

    def check_product_price(self):
        expect(self.product_price).to_be_visible()

    def check_product_availability(self):
        expect(self.product_availability).to_be_visible()

    def check_product_coniditon(self):
        expect(self.product_condition).to_be_visible()

    def check_product_brand(self):
        expect(self.product_brand).to_be_visible()



