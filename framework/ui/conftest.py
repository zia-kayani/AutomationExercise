import pytest
from framework.common.config.config import Config


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


