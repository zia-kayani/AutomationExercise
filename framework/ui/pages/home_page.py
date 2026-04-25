from framework.ui.locators.home_locators import HomeLocators as loc
from playwright.sync_api import expect


class HomePage:
    def __init__(self, page):
        self.page = page

    # ---------------- PROPERTIES ----------------

    @property
    def subscription_text(self):
        return loc.SUBSCRIPTION_TEXT(self.page)

    @property
    def automation_sub_heading(self):
        return loc.AUTOMATION_EXERCISE_SUB_HEADING(self.page)

    # ---------------- ACTIONS ----------------

    def check_subscription_text_visible(self):
        expect(self.subscription_text).to_be_visible()

    def check_home_sub_heading_visible(self):
        expect(self.automation_sub_heading).to_be_visible()

    def scroll_to_subscription_section(self):
        self.subscription_text.scroll_into_view_if_needed()

    def scroll_to_sub_heading(self):
        self.automation_sub_heading.scroll_into_view_if_needed()