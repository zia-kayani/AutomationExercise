import pytest
from framework.common.config.config import Config

# Remove custom context fixture - let pytest-playwright handle browser/context
# The browser and page fixtures are provided by pytest-playwright plugin

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


