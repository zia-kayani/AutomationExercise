class TestCasesLocators:

    # TEST_CASES_PAGE_BUTTON = lambda page: page.locator("a[href='/test_cases']:has-text('Test Cases')")
    TEST_CASES_PAGE_BUTTON = lambda page: page.get_by_role("link", name="Test Cases", exact=True)
    TEST_CASES_PAGE_INSTRUCTIONS = lambda page: page.locator("span", has_text="Below is the list of test Cases")

    