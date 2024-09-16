from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

from setup_browser import set_browser  # Импортируем функцию setup_browser

def test_google_title(driver):
    """
    Тест для проверки заголовка страницы Google.
    """
    sleep(100)
    driver.get("https://www.google.com")
    title = driver.title
    assert title == "Google"
    sleep(100000)
