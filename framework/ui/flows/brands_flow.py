from framework.ui.pages.brands_page import BrandsPage


class BrandsFlow:
    def __init__(self, page):
        self.brands_page = BrandsPage(page)

    def open_polo_brand_and_verify(self):
        self.brands_page.verify_brands_section_visible()
        self.brands_page.click_polo_brand()
        self.brands_page.verify_polo_brand_page()

    def open_hm_brand_and_verify(self):
        self.brands_page.verify_brands_section_visible()
        self.brands_page.click_hm_brand()
        self.brands_page.verify_hm_brand_page()