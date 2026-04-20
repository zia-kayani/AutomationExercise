class EmailSubscriptionLocators:

    FOOTER =  lambda page: page.locator("#footer")
    
    SUBSCRIPTION_TEXT =  lambda page: page.get_by_text("SUBSCRIPTION")

    
    SUBSCRIBE_EMAIL_INPUT = lambda page: page.locator('input#susbscribe_email[type="email"]')

    SUBSCRIBE_EMAIL_BUTTON = lambda page: page.locator('button#subscribe.btn.btn-default')

    SUBSCRIBE_SUCCESS_MESSAGE =  lambda page: page.get_by_text("You have been successfully subscribed!")

