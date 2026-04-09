class ContactUsLocators:

    CONTACT_UR_LINK = lambda page: page.get_by_role("link", name="Contact us")
    GET_IN_TOUCH_HEADING = lambda page: page.get_by_role("heading", name="Get In Touch")
    NAME_INPUT_CONTACT_US = lambda page: page.locator("[data-qa='name']")
    EMAIL_INPUT_CONTACT_US = lambda page: page.locator("[data-qa='email']")
    SUBJECT_INPUT_CONTACT_US = lambda page: page.locator("[data-qa='subject']")
    MESSAGE_TEXTAREA_CONTACT_US = lambda page: page.locator("[data-qa='message']")
    UPLOAD_FILE_INPUT_CONTACT_US = lambda page: page.locator("input[name='upload_file']")
    SUBMIT_BUTTON_CONTACT_US = lambda page: page.locator("[data-qa='submit-button']")
    SUCCESS_MESSAGE_CONTACT_US = lambda page: page.locator("#contact-page .alert-success")
    
    HOME_LINK_CONTACT_US = lambda page: page.locator("a.btn.btn-success") 

