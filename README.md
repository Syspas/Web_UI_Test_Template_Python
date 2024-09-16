## README.md

### Тестовый проект с использованием Selenium и Firefox

Этот проект демонстрирует автоматизацию тестирования в Firefox с использованием Selenium и расширений.

Описание:

- Проект использует Selenium для взаимодействия с браузером.
- В качестве браузера используется Firefox с установленным расширением firefox_cryptopro_extension_latest.xpi.
- Встроен базовый тест для проверки заголовка страницы Google.

Установка:

1. Установите Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Установите необходимые библиотеки:
   pip install selenium pytest webdriver-manager

3. Скачайте GeckoDriver: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
4. Установите расширение CryptoPro: Загрузите файл firefox_cryptopro_extension_latest.xpi  в директорию src/main/resources вашего проекта.

Использование:

1. Настройка браузера:
    - Откройте файл setup_browser.py.
    - Укажите правильный путь к geckodriver.exe в константе GECKODRIVER_PATH.
    - Убедитесь, что файл firefox_cryptopro_extension_latest.xpi находится в директории src/main/resources.

2. Запуск тестов:
    - Запустите тесты с помощью PyTest: pytest.

Пример теста:

- В файле test_google.py вы можете найти простой тест, который открывает Google и проверяет заголовок страницы.

Дополнительные замечания:

- Для работы проекта необходимы: Python, Selenium, PyTest, WebDriverManager, GeckoDriver, расширение firefox_cryptopro_extension_latest.xpi.
- Для запуска тестов в headless режиме, раскомментируйте строки с  driver.set_window_size(1, 1) и driver.set_window_position(-10000, -10000) в  setup_browser.py.

Автор:
[Ваше имя]

Лицензия:
[Ваша лицензия]