class EmailSubscriptionLocators:

    FOOTER =  lambda page: page.locator("#footer")
    
    SUBSCRIPTION_TEXT =  lambda page: page.get_by_text("SUBSCRIPTION")

    
    SUBSCRIBE_EMAIL_INPUT = lambda page: page.locator('input#susbscribe_email[type="email"]')

    SUBSCRIBE_EMAIL_BUTTON = lambda page: page.locator('button#subscribe.btn.btn-default')

    SUBSCRIBE_SUCCESS_MESSAGE =  lambda page: page.get_by_text("You have been successfully subscribed!")

    #locators for cart page email subscription 
    CART_PAGE_LINK = lambda page: page.locator('a[href="/view_cart"]:has(i.fa-shopping-cart)')

