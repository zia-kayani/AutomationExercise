
class CartLocators:
    #cart page Link
    CART_PAGE_LINK = lambda page: page.get_by_role("link", name="Cart")
    
    # product containers
    FIRST_PRODUCT = lambda page: page.locator(".product-image-wrapper").first
    SECOND_PRODUCT = lambda page: page.locator(".product-image-wrapper").nth(1)

    # child selector (IMPORTANT: string, not locator)
    PRODUCT_OVERLAY_ADD_TO_CART_BUTTON = ".product-overlay a.add-to-cart"

    # global elements
    CONTINUE_SHOPPING_BUTTON = lambda page: page.get_by_role("button", name="Continue Shopping")
    VIEW_CART_BUTTON = lambda page: page.get_by_role("link", name="View Cart")
    FIRST_PRODUCT_NAME =  lambda page: page.locator("a[href='/product_details/1']", has_text="Blue Top")
    SECOND_PRODUCT_NAME =  lambda page: page.locator("a[href='/product_details/2']", has_text="Men Tshirt")

    # Locator for general products
    PRODUCT_ADD_TO_CART_BUTTON =  lambda page: page.locator("button.btn.cart:has-text('Add to cart')")

    PRODUCT_QUANTITY_IN_CART = lambda page:     page.locator("button.disabled")


