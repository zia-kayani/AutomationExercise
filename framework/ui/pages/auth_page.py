# framework/ui/pages/auth_page.py

from framework.ui.locators.auth_locators import AuthLocators as loc


class AuthPage:

    def __init__(self, page):
        self.page = page
    
    #------------------------------------------ Properties ------------------------------------------

    # --------Common  Properties for Signup/Login    --------
    @property
    def signup_login_link(self):
        return loc.SIGNUP_LOGIN_LINK(self.page)
    
    @property
    def home_link(self):
        return loc.HOME_lINK(self.page)
    
    # -------- Properties for Signup --------

    @property
    def name_input(self):
        return loc.NAME_INPUT(self.page)

    @property
    def email_input(self):
        return loc.EMAIL_INPUT(self.page)

    @property
    def signup_button(self):
        return loc.SIGNUP_BUTTON(self.page)

    @property
    def heading(self):
        return loc.HEADING(self.page)

    @property
    def title_mrs(self):
        return loc.TITLE_MRS(self.page)

    @property
    def password_input(self):
        return loc.PASSWORD_INPUT(self.page)

    @property
    def day_dropdown(self):
        return loc.DAY_DROPDOWN(self.page)

    @property
    def month_dropdown(self):
        return loc.MONTH_DROPDOWN(self.page)

    @property
    def year_dropdown(self):
        return loc.YEAR_DROPDOWN(self.page)

    @property
    def first_name(self):
        return loc.FIRST_NAME(self.page)

    @property
    def last_name(self):
        return loc.LAST_NAME(self.page)

    @property
    def company(self):
        return loc.COMPANY(self.page)

    @property
    def address(self):
        return loc.ADDRESS(self.page)

    @property
    def address2(self):
        return loc.ADDRESS2(self.page)

    @property
    def country(self):
        return loc.COUNTRY(self.page)

    @property
    def state(self):
        return loc.STATE(self.page)

    @property
    def city(self):
        return loc.CITY(self.page)

    @property
    def zipcode(self):
        return loc.ZIPCODE(self.page)

    @property
    def mobile(self):
        return loc.MOBILE(self.page)

    @property
    def create_account_btn(self):
        return loc.CREATE_ACCOUNT_BTN(self.page)

    @property
    def account_created_text(self):
        return loc.ACCOUNT_CREATED_TEXT(self.page)

    @property
    def continue_btn(self):
        return loc.CONTINUE_BTN(self.page)

    @property
    def logout_link(self):
        return loc.LOGOUT_LINK(self.page)

    @property
    def delete_account_link(self):
        return loc.DELETE_ACCOUNT_LINK(self.page)
    
    #email already exists property
    @property
    def email_already_exists_text(self):
        return loc.EMAIL_ALREADY_EXISTS_TEXT(self.page)
    
    # -------- Properties for Login --------

    @property
    def login_heading(self):
        return loc.LOGIN_TO_HEADING(self.page)
    
    @property
    def login_email_input(self):
        return loc.LOGIN_EMAIL_INPUT(self.page)
    
    @property
    def login_password_input(self):
        return loc.LOGIN_PASSWORD_INPUT(self.page)
    
    @property
    def login_button(self):
        return loc.LOGIN_BUTTON(self.page)
    
    @property
    def logged_in_as(self):
        return loc.LOGGED_IN_AS(self.page)
    
    @property
    def delete_account_link_after_login(self):
        return loc.DELETE_ACCOUNT_LINK(self.page)
    
    @property
    def account_deleted_text(self):
        return loc.ACCOUNT_DELETED_TEXT(self.page)
    

    # login with invalid credentials property
    @property
    def incorrect_email_password_text(self):
        return loc.INCORRECT_EMAIL_PASSWORD_TEXT(self.page)
    
    #logout  properties
    @property
    def logout_link(self):
        return loc.LOGOUT_LINK(self.page)
    

    #-------------------------------------Actions-------------------------------------

    # --------Common Actions --------
    def home_page_link(self):
        return self.home_link.is_visible()
    

    def go_to_signup_login(self):
        self.signup_login_link.click()
        self.name_input.wait_for(state="visible")

    #   ------ Actions for Signup --------
    def signup(self, name: str, email: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()

    def fill_account_info(self, password, day, month, year):
        self.title_mrs.check()
        self.password_input.fill(password)
        self.day_dropdown.select_option(day)
        self.month_dropdown.select_option(month)
        self.year_dropdown.select_option(year)

    def fill_address_info(self, first, last, company, address, address2,
                          country, state, city, zipcode, mobile):

        self.first_name.fill(first)
        self.last_name.fill(last)
        self.company.fill(company)
        self.address.fill(address)
        self.address2.fill(address2)
        self.country.select_option(country)
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobile.fill(mobile)

    def create_account(self):
        self.create_account_btn.click()

    def continue_after_registration(self):
        self.continue_btn.click()

    def logout(self):
        self.logout_link.click()

    def delete_account(self):
        self.delete_account_link.click()

    #action for email already exists
    def email_already_exists_text_visible(self):
        return self.email_already_exists_text.is_visible()

    # -------- Actions for Login --------
    def login_heading_visible(self):
        return self.login_heading.is_visible()
    
    def enter_login_email(self, email):
        self.login_email_input.fill(email)

    def enter_login_password(self, password):
        self.login_password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def logged_in_as_visible(self):
        return self.logged_in_as.is_visible()
    
    def delete_account_after_login(self):
        self.delete_account_link_after_login.click()

    def account_deleted_text_visible(self):
        return self.account_deleted_text.is_visible()
    
    # login with invalid credentials action
    def incorrect_email_password_text_visible(self):
        return self.incorrect_email_password_text.is_visible()
    
    #logout action
    def click_logout(self):
        self.logout_link.click()

    

    