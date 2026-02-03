# conftest.py
import pytest
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    """Создание драйвера Chrome для каждого теста"""
    print("\n" + "="*60)
    print("настройка driver...")
    
    chrome_options = Options()
    
    # ВАЖНО: закомментируйте headless для первого запуска!
    # chrome_options.add_argument("--headless")
    
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    # Путь к вашему скачанному драйверу
    driver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
    
    print(f"Ищем драйвер по пути: {driver_path}")
    print(f"Драйвер существует: {os.path.exists(driver_path)}")
    
    if not os.path.exists(driver_path):
        print("\n ОШИБКА: ChromeDriver не найден!")
        print("Убедитесь, что chromedriver.exe находится в папке проекта")
        print("Текущая папка:", os.path.dirname(__file__))
        print("\nСодержимое папки:")
        for file in os.listdir(os.path.dirname(__file__)):
            if "chrome" in file.lower():
                print(f"  - {file}")
        print("="*60)
        raise FileNotFoundError(f"ChromeDriver не найден: {driver_path}")
    
    print("Драйвер найден!")
    print("="*60)
    
    try:
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("Драйвер успешно инициализирован!")
        return driver
    except Exception as e:
        print(f"Ошибка при создании драйвера: {e}")
        print("\nПопробуйте:")
        print("1. Удалить chromedriver.exe")
        print("2. Скачать заново с https://chromedriver.chromium.org/")
        print("3. Выбрать версию, соответствующую вашему Chrome")
        raise


@pytest.fixture(scope="function")
def login_page(driver):
    """Создание страницы логина"""
    print("Создаем страницу логина...")
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Создание скриншотов при падении тестов"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")