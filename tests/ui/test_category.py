import pytest
from framework.ui.flows.category_flow import CategoriesFlow

class TestCategories:

    #TC-18 View Category Products Test Case
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.ui
    def test_verify_product_categories(self, page):

        flow = CategoriesFlow(page)
        #Step1 and 2: lanuch the prowser and open project
        
        # Step 3: Verify categories visible
        flow.verify_left_sidebar_categories()

        # Step 4–6: Women category flow
        flow.select_women_dress_category()
        flow.verify_women_category_page()

        # Step 7–8: Men category flow
        flow.select_men_tshirts_category()
        flow.verify_men_category_page()