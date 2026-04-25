class CheckoutLocators:

    PROCEED_TO_CHECKOUT_BUTTON = lambda page: page.locator("a.check_out")

    CHECKOUT_REGISTER_LOGIN_LINK =  lambda page: page.get_by_role("link", name="Register / Login")

    ADDRESS_DETAILS_HEADING = lambda page: page.get_by_role("heading", name="Address Details")

    COMMENT_TEXT_AREAD_INPUT = lambda page: page.locator("textarea[name='message']")
    
    PLACE_ORDER_BUTTON = lambda page: page.get_by_role("link", name="Place Order")

    #card details
    NAME_ON_CARD =  lambda page: page.locator("[data-qa='name-on-card']")
    CARD_NUMBER = lambda page: page.locator("[data-qa='card-number']")
    CVC = lambda page: page.locator("[data-qa='cvc']")
    EXPIRY_MONTH = lambda page: page.locator("[data-qa='expiry-month']")
    EXPIRY_YEAR =  lambda page: page.locator("[data-qa='expiry-year']")

    PAY_AND_CONFRIM_BUTTON = lambda page: page.locator("[data-qa='pay-button']")

    ORDER_CONFIRMATION_MESSAGE = lambda page: page.get_by_text("Congratulations! Your order has been confirmed!")

    #Verify address deatil in checkout page
    CHECKPUT_PAGE_ADDRESS = lambda page: page.locator("#address_delivery li.address_city.address_state_name.address_postcode")

    #download invoice button 
    DOWNLOAD_INVOICE_BUTTON_AFTER_DOWNLOAD = lambda page: page.locator("a.btn.btn-default.check_out")