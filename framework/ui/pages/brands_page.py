from framework.ui.locators.brands_locators import BrandsLocators as loc
from playwright.sync_api import expect


class BrandsPage:
    def __init__(self, page):
        self.page = page


    @property
    def brands_heading(self):
        return loc.BRANDS_HEADING(self.page)

    @property
    def brands_list(self):
        return loc.BRANDS_LIST(self.page)

    @property
    def polo_brand(self):
        return loc.POLO_BRAND(self.page)

    @property
    def polo_brand_heading(self):
        return loc.POLO_BRAND_PAGE_HEADING(self.page)

    @property
    def hm_brand(self):
        return loc.H_AND_M_BRAND(self.page)

    @property
    def hm_brand_heading(self):
        return loc.H_AND_M_BRAND_PAGE_HEADING(self.page)

    # ACTIONS

    def verify_brands_section_visible(self):
        expect(self.brands_heading).to_be_visible()

    def click_polo_brand(self):
        self.polo_brand.click()

    def click_hm_brand(self):
        self.hm_brand.click()

    def verify_polo_brand_page(self):
        expect(self.polo_brand_heading).to_be_visible()

    def verify_hm_brand_page(self):
        expect(self.hm_brand_heading).to_be_visible()