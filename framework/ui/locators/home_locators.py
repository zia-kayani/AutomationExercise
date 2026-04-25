class HomeLocators:
    SUBSCRIPTION_TEXT =  lambda page: page.get_by_text("SUBSCRIPTION")

    AUTOMATION_EXERCISE_SUB_HEADING = lambda page:  page.get_by_role("heading", name="Full-Fledged practice website for Automation Engineers")
