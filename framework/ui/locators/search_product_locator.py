class SearchProductLocators:

    SEARCH_INPUT  = lambda page: page.locator("input[name='search']")

    SEARCH_BUTTON =  lambda page: page.locator("button#submit_search")

    PRODUCT_DETAILS_LINK = lambda page: page.get_by_role("link", name="View Product").first

