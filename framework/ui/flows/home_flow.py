from framework.ui.pages.home_page import HomePage


class HomeFlow:
    def __init__(self, page):
        self.home_page = HomePage(page)

    def verify_subscription_section(self):
        self.home_page.scroll_to_subscription_section()
        self.home_page.check_subscription_text_visible()

    def verify_home_sub_heading(self):
        self.home_page.scroll_to_sub_heading()
        self.home_page.check_home_sub_heading_visible()