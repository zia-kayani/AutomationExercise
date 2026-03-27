import pytest

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context):
    page =  context.new_page()
    yield page
    page.close()
