from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

# Константы
GECKODRIVER_PATH = "geckodriver.exe"  # Замените на ваш путь
FIREFOX_EXTENSION_PATH = "D:\\VCS\\SVN\\PythonTest\\firefox_cryptopro_extension_latest.xpi"  # Замените на ваш путь


def set_browser():
    options = Options()
    options.add_argument("--disable-extensions")  # Отключить все расширения
    options.add_argument(f"--load-extension={FIREFOX_EXTENSION_PATH}")  # Загрузить только CryptoPro
    #options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    #driver = webdriver.Firefox(service=service)
    driver.install_addon('FIREFOX_EXTENSION_PATH')

    # Настройка браузера (необязательно)
    driver.set_window_size(1920, 1080)
    return driver