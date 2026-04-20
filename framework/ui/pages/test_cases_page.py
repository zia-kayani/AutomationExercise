from framework.ui.locators.test_cases_locators import TestCasesLocators as loc

class TestCasesPage:
    def __init__(self, page):
        self.page = page

    @property
    def test_cases_page_button(self):
        return loc.TEST_CASES_PAGE_BUTTON(self.page)
    
    @property
    def test_cases_page_instructions(self):
        return  loc.TEST_CASES_PAGE_INSTRUCTIONS(self.page)
    
    def navigate_to_test_cases_page(self):
        self.test_cases_page_button.click()

    def verify_test_cases_page_instructions(self):
        return self.test_cases_page_instructions.is_visible()
    



