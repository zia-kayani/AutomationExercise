# framework/ui/locators/auth_locators.py

class AuthLocators:

    # -------- Common --------
    SIGNUP_LOGIN_LINK = lambda page: page.get_by_role("link", name="Signup / Login")

    # -------- Signup (Homepage) --------
    NAME_INPUT = lambda page: page.locator('[data-qa="signup-name"]')
    EMAIL_INPUT = lambda page: page.locator('[data-qa="signup-email"]')
    SIGNUP_BUTTON = lambda page: page.get_by_role("button", name="Signup")

    # -------- Register Page --------
    HEADING = lambda page: page.get_by_role("heading", name="Enter Account Information")
    TITLE_MRS = lambda page: page.get_by_role("radio", name="Mrs.")
    PASSWORD_INPUT = lambda page: page.get_by_label("Password *")

    DAY_DROPDOWN = lambda page: page.locator("#days")
    MONTH_DROPDOWN = lambda page: page.locator("#months")
    YEAR_DROPDOWN = lambda page: page.locator("#years")

    FIRST_NAME = lambda page: page.get_by_label("First name *")
    LAST_NAME = lambda page: page.get_by_label("Last name *")
    COMPANY = lambda page: page.get_by_label("Company", exact=True)

    ADDRESS = lambda page: page.locator('[data-qa="address"]')
    ADDRESS2 = lambda page: page.get_by_label("Address 2")

    COUNTRY = lambda page: page.get_by_label("Country *")
    STATE = lambda page: page.get_by_label("State *")
    CITY = lambda page: page.get_by_label("City *")
    ZIPCODE = lambda page: page.locator("#zipcode")

    MOBILE = lambda page: page.get_by_label("Mobile Number *")

    CREATE_ACCOUNT_BTN = lambda page: page.get_by_role("button", name="Create Account")

    # -------- Success --------
    ACCOUNT_CREATED_TEXT = lambda page: page.get_by_text("Account Created!")
    CONTINUE_BTN = lambda page: page.get_by_role("link", name="Continue")

    # -------- Home --------
    LOGOUT_LINK = lambda page: page.get_by_role("link", name="Logout")
    DELETE_ACCOUNT_LINK = lambda page: page.get_by_role("link", name="Delete Account")
