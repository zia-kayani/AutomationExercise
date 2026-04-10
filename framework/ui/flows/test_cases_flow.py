from framework.ui.pages.auth_page import AuthPage
from framework.ui.pages.test_cases_page import TestCasesPage

class TestCasesFlow:

    def __init__(self, page):
        self.auth_page = AuthPage(page)
        self.test_cases_page = TestCasesPage(page)

    def home_page_visible(self):
        self.auth_page.home_page_link()

    def navigate_to_test_cases_page(self):
        self.test_cases_page.navigate_to_test_cases_page()
    
    def verify_test_cases_page_instructions(self):
        return self.test_cases_page.verify_test_cases_page_instructions()

