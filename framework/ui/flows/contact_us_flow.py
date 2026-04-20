from framework.ui.pages.contact_us_page import ContactUsPage


class ContactUsFlow:

    def __init__(self, page):
        self.contact_us_page = ContactUsPage(page)


    def submit_contact_form(self, name, email, subject, message, file_name):
        self.contact_us_page.click_contact_us()
        assert self.contact_us_page.contact_us_heading_visible(), "Get in touch heading not visible, might not be on contact us page"
        self.contact_us_page.fill_contact_form(name, email, subject, message)
        self.contact_us_page.upload_file(file_name)
        self.contact_us_page.click_submit_button()

        self.contact_us_page.page.once("dialog", lambda dialog: dialog.accept())

    def go_to_home_page(self):
        self.contact_us_page.click_on_home_page()
    


    