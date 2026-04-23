from framework.ui.pages.category_page import CategoriesPage

class CategoriesFlow:

    def __init__(self, page):
        self.page = page
        self.categories_page = CategoriesPage(page)

    def verify_left_sidebar_categories(self):
        self.categories_page.verify_categories_visible()

    def select_women_dress_category(self):
        self.categories_page.open_women_category()
        self.categories_page.open_women_dress()

    def verify_women_category_page(self):
        self.categories_page.verify_women_dress_page()

    def select_men_tshirts_category(self):
        self.categories_page.open_men_category()
        self.categories_page.open_men_tshirts()

    def verify_men_category_page(self):
        self.categories_page.verify_men_tshirts_page()