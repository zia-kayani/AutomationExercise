import pytest
from framework.ui.flows.contact_us_flow import ContactUsFlow
from framework.ui.flows.auth_flow import AuthFlow
import time 


class TestContactUs:


    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.parametrize("name, email, subject, message, file_path", [
        ("Test User", "test@example.com", "Test Subject", "Test Message for contact us form submission", "test-file.pdf")
    ])
    def test_contact_us_form_submission(self, page, name, email, subject, message, file_path):
        flow = ContactUsFlow(page)
        home_flow = AuthFlow(page)
        assert home_flow.home_page_visible(), "home page is not visible"
        flow.submit_contact_form(name, email, subject, message, file_path)
        flow.go_to_home_page()
