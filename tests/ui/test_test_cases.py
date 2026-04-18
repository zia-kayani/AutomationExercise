import pytest

from framework.ui.flows.test_cases_flow import TestCasesFlow

class TestTestCases:

    #TC: Verify that user can navigate to test cases page and see the instructions along with test cases list 
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    def test_cases(self, page):
        flow = TestCasesFlow(page)

        flow.home_page_visible()
        flow.navigate_to_test_cases_page()
        assert flow.verify_test_cases_page_instructions(), \
            "Test cases page instructions not visible, might not be on test cases page"
