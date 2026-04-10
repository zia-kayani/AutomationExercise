from framework.ui.locators.test_cases_locators import TestCasesLocators 

class TestCasesPage:
    def __init__(self, page):
        self.page = page
        self.locators = TestCasesLocators()

    @property
    def test_cases_page_button(self):
        return self.locators.TEST_CASES_PAGE_BUTTON
    
    @property
    def test_cases_page_instructions(self):
        return self.locators.TEST_CASES_PAGE_INSTRUCTIONS
    
    def navigate_to_test_cases_page(self):
        self.test_cases_page_button(self.page).click()

    def verify_test_cases_page_instructions(self):
        return self.test_cases_page_instructions(self.page).is_visible()