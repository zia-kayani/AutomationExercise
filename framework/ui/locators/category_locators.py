class CategoriesLocators:
    CATEGORY_HEADING = lambda page: page.locator("h2:has-text('Category')")

    WOMEN_CATEGORY_LINK = lambda page: page.locator("a[href='#Women']")
    WOMEN_DRESS_SUBCATEGORY = lambda page: page.locator("a[href='/category_products/1']")

    WOMEN_DRESS_SUBCATEGORY_PAGE_HEADING = lambda page: page.locator("h2.title:has-text('Women - Dress Products')")

    MEN_CATEGORY_LINK = lambda page: page.locator("a[href='#Men']")
    MEN_TSHIRTS_SUBCATEGORY = lambda page: page.locator("a[href='/category_products/3']")
    MEN_TSHIRTS_SUBCATEGORY_PAGE_HEADING =lambda page: page.locator("h2.title:has-text('Men - Tshirts Products')")

    KIDS_CATEGORY_LINK = lambda page: page.locator("a[href='#Kids']")
