import pytest
from framework.ui.flows.home_flow import HomeFlow


class TestHome:
    #TC 25 & 26 -- Verify Scroll Up without 'Arrow' button and Scroll Down functionality
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    def test_home_page_elements_visibility(self, page):

        home_flow = HomeFlow(page)

        # verify subscription section
        home_flow.verify_subscription_section()

        # verify main heading
        home_flow.verify_home_sub_heading()