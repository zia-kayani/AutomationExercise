from framework.ui.locators.contact_us_locators import ContactUsLocators as loc
from pathlib import Path
from playwright.sync_api import expect


class ContactUsPage:

    def __init__(self, page):

        self.page = page

    #-------------------------------Properties-------------------------------------

    @property
    def contact_us_link(self):
        return loc.CONTACT_UR_LINK(self.page)
    
    @property
    def get_in_touch_heading(self):
        return loc.GET_IN_TOUCH_HEADING(self.page)
    
    @property
    def name_input(self):
        return loc.NAME_INPUT_CONTACT_US(self.page)
    
    @property
    def email_input(self):
        return loc.EMAIL_INPUT_CONTACT_US(self.page)
    
    @property
    def subject_input(self):
        return loc.SUBJECT_INPUT_CONTACT_US(self.page)
    
    @property
    def message_textarea(self):
        return loc.MESSAGE_TEXTAREA_CONTACT_US(self.page)
    
    @property
    def upload_file_input(self):
        return loc.UPLOAD_FILE_INPUT_CONTACT_US(self.page)
    
    @property
    def submit_button(self):
        return loc.SUBMIT_BUTTON_CONTACT_US(self.page)
    
    @property
    def success_message(self):
        return loc.SUCCESS_MESSAGE_CONTACT_US(self.page)
    
    @property
    def home_link(self):
        return loc.HOME_LINK_CONTACT_US(self.page)
    
    # -------------------------------Actions-------------------------------------
    def click_contact_us(self):
        self.contact_us_link.click()

    def contact_us_heading_visible(self):
        return self.get_in_touch_heading.is_visible()
    
    def fill_contact_form(self, name, email, subject, message):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_textarea.fill(message)




    def upload_file(self, filename):
        file_path = Path("test-data") / filename
        if not file_path.exists():
            raise FileNotFoundError(f"{file_path} does not exist")
        self.upload_file_input.set_input_files(file_path)


    def submit_contact_form(self):
        self.submit_button.click()
    
    def verify_success_message(self):
        expect(self.success_message).to_be_visible()    
        
    def navigate_to_home(self):
        self.home_link.click()
    