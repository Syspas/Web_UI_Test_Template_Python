import pytest
from setup_browser import set_browser

@pytest.fixture
def driver():
    """
    Фикстура для создания браузера.
    """
    driver = set_browser()
    yield driver
    driver.quit()
