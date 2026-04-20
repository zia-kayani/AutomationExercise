import pytest
from playwright.sync_api import sync_playwright
from framework.common.config.config import Config


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(
        headless=Config.HEADLESS   
    )
    yield browser
    browser.close()


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