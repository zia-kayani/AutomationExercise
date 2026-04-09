import pytest
from framework.ui.flows.contact_us_flow import ContactUsFlow



class TestContactUs:


    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.parametrize("name, email, subject, message, file_path", [
        ("Test User", "test@example.com", "Test Subject", "Test Message for contact us form submission", "test-file.pdf")
    ])
    def test_contact_us_form_submission(self, page, name, email, subject, message, file_path):
        flow = ContactUsFlow(page)

        assert flow.home_page_visible(), "Home page is not visible"
        flow.submit_contact_form(name, email, subject, message, file_path)
        flow.verify_success_message(), "Success message not visible, form submission might have failed"
        flow.navigate_back_to_home()
        assert flow.home_page_visible(), "Home page is not visible after navigating back, might not have navigated back correctly"
