from framework.ui.pages.contact_us_page import ContactUsPage
from framework.ui.pages.auth_page import AuthPage 


class ContactUsFlow:

    def __init__(self, page):
        self.contact_us_page = ContactUsPage(page)
        self.auth_page = AuthPage(page)

    def home_page_visible(self):
        return self.auth_page.home_page_link()
        
    def submit_contact_form(self, name, email, subject, message, file_path):
        self.contact_us_page.click_contact_us()
        assert self.contact_us_page.contact_us_heading_visible(), "Get in touch heading not visible, might not be on contact us page"
        self.contact_us_page.fill_contact_form(name, email, subject, message)
        self.contact_us_page.upload_file(file_path)

        self.contact_us_page.page.once("dialog", lambda dialog: dialog.accept())

        self.contact_us_page.submit_contact_form()

    def verify_success_message(self):
        self.contact_us_page.verify_success_message()
    
    def navigate_back_to_home(self):
        self.contact_us_page.navigate_to_home()
    


    