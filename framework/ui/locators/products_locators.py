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
