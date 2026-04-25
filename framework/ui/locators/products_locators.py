class ProductsLocators:

    PRODUCTS_PAGE_LINK = lambda page: page.get_by_role("link" , name="Products")

    PRODUCTS_PAGE_URL =  "https://automationexercise.com/products"

    FEATURED_PRODUCTS_LIST = lambda page: page.locator(".features_items")

    FIRST_PRODUCT_VIEW_PRODUCT_BUTTON = lambda page: page.locator("a[href='/product_details/1']")

    #single product 
    PRODUCT_NAME= lambda page: page.locator(".product-information h2")
    PRODUCT_CATEGORY = lambda page : page.locator(".product-information p").filter(has_text="Category")
    PRODUCT_PRICE = lambda page: page.locator(".product-information span").first
    PRODUCT_AVAILABILITY = lambda page: page.locator(".product-information p:has-text('Availability')")
    PRODUCT_CONDITION = lambda page: page.locator(".product-information p:has-text('Condition')")
    PRODUCT_BRAND  = lambda page: page.locator(".product-information p:has-text('Brand')")

    
    PRODUCT_QUANTITY_INPUT =  lambda page: page.locator("#quantity")


    #product reiview 
    PRODUCT_REVIEW_HEADING = lambda page: page.get_by_text("Write Your Review")
    PRODUCT_REVIEW_NAME_INPUT = lambda page: page.locator('input[id="name"]')
    PRODUCT_REVIEW_EMAIL_INPUT = lambda page: page.locator('input[id="email"]')
    PRODUCT_REIVIEW_MESSAGE_INPUT = lambda page: page.locator('textarea[name="review"]')
    PRODUCT_REVIEW_SUBMIT_BUTTON =  lambda page: page.locator('#button-review')
    PRODUCT_REVIEW_SUCCESS_MESSAGE =  lambda page: page.locator('span:has-text("Thank you for your review.")');

    #Recommended products
    RECOMENDED_PRODUCTS_HEADING =  lambda page: page.get_by_role("heading", name="recommended items")

