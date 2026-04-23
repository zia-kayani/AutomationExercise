class BrandsLocators:
    BRANDS_HEADING = lambda page: page.get_by_role("heading", name="Brands")

    BRANDS_LIST =  lambda page: page.locator(".brands-name ul.nav")

    POLO_BRAND = lambda page: page.locator("a[href='/brand_products/Polo']")    
    POLO_BRAND_PAGE_HEADING =  lambda page: page.get_by_role("heading", name="Brand - Polo Products")

    H_AND_M_BRAND = lambda page: page.locator("a[href='/brand_products/H&M']")   
    H_AND_M_BRAND_PAGE_HEADING =  lambda page: page.get_by_role("heading", name="Brand - H&M Products")
 
