import pytest
from framework.common.config.config import Config

@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()

    if not Config.BASE_URL:
        raise ValueError("BASE_URL is not set in environment variables")
    page.goto(Config.BASE_URL)


    yield page
    page.close()

    