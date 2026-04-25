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
    
    @property
    def product_quantity_input(self):
        return loc.PRODUCT_QUANTITY_INPUT(self.page)
    
    #product review
    @property
    def product_review_name_input(self):
        return loc.PRODUCT_REVIEW_NAME_INPUT(self.page)
    
    @property
    def product_review_email_input(self):
        return loc.PRODUCT_REVIEW_EMAIL_INPUT(self.page)

    @property
    def product_review_message_input(self):
        return loc.PRODUCT_REIVIEW_MESSAGE_INPUT(self.page)

    @property
    def product_review_submit_button(self):
        return loc.PRODUCT_REVIEW_SUBMIT_BUTTON(self.page)

    @property
    def product_review_success_message(self):
        return loc.PRODUCT_REVIEW_SUCCESS_MESSAGE(self.page)
    
    @property
    def product_review_success_message(self):
        return loc.PRODUCT_REVIEW_SUCCESS_MESSAGE(self.page)
    
    # Recommended product 
    
    @property
    def recommended_products_heading(self):
        return loc.RECOMENDED_PRODUCTS_HEADING(self.page)
    

    #----actions ----------------------------------------------------

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

    
    def increase_decrease_product_quantity(self, value:str):
        self.product_quantity_input.fill(value)

    #Product review actions
    
    def fill_product_review_name(self, name: str):
        self.product_review_name_input.fill(name)

    def fill_product_review_email(self, email: str):
        self.product_review_email_input.fill(email)

    def fill_product_review_message(self, message: str):
        self.product_review_message_input.fill(message)

    def submit_product_review(self):
        self.product_review_submit_button.click()

    def check_product_review_success_message(self):
        expect(self.product_review_success_message).to_be_visible()

    #recommended products
    def check_recommended_products_heading(self):
        self.recommended_products_heading.scroll_into_view_if_needed()
        expect(self.recommended_products_heading).to_be_visible()
