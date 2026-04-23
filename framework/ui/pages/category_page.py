from playwright.sync_api import expect
from framework.ui.locators.category_locators import CategoriesLocators as loc


class CategoriesPage:

    def __init__(self, page):
        self.page = page

    # ---------------- Properties ----------------

    @property
    def category_heading(self):
        return loc.CATEGORY_HEADING(self.page)

    @property
    def women_category_link(self):
        return loc.WOMEN_CATEGORY_LINK(self.page)

    @property
    def women_dress_subcategory(self):
        return loc.WOMEN_DRESS_SUBCATEGORY(self.page)

    @property
    def women_dress_heading(self):
        return loc.WOMEN_DRESS_SUBCATEGORY_PAGE_HEADING(self.page)

    @property
    def men_category_link(self):
        return loc.MEN_CATEGORY_LINK(self.page)

    @property
    def men_tshirts_subcategory(self):
        return loc.MEN_TSHIRTS_SUBCATEGORY(self.page)

    @property
    def men_tshirts_heading(self):
        return loc.MEN_TSHIRTS_SUBCATEGORY_PAGE_HEADING(self.page)

    @property
    def kids_category_link(self):
        return loc.KIDS_CATEGORY_LINK(self.page)

    # ---------------- Actions ----------------

    def verify_categories_visible(self):
        expect(self.category_heading).to_be_visible()

    def open_women_category(self):
        self.women_category_link.click()

    def open_women_dress(self):
        self.women_dress_subcategory.click()

    def verify_women_dress_page(self):
        expect(self.women_dress_heading).to_be_visible()

    def open_men_category(self):
        self.men_category_link.click()

    def open_men_tshirts(self):
        self.men_tshirts_subcategory.click()

    def verify_men_tshirts_page(self):
        expect(self.men_tshirts_heading).to_be_visible()