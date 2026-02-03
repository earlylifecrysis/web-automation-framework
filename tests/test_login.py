# tests/test_login.py
import pytest
import allure
import time
from utils.config import Config


@allure.epic("Тестирование авторизации")
@allure.feature("Логин")
class TestLogin:
    """5 тестов для проверки логина на SauceDemo"""
    
    @allure.story("Успешная авторизация")
    @allure.title("Тест 1: Успешный логин с валидными данными")
    def test_successful_login(self, login_page):
        """Тест успешного логина стандартного пользователя"""
        with allure.step("Выполнение успешного логина"):
            login_page.login(Config.VALID_USER, Config.VALID_PASSWORD)
            time.sleep(2)
        
        with allure.step("Проверка перехода на страницу товаров"):
            current_url = login_page.driver.current_url
            assert "/inventory.html" in current_url, \
                f"Ожидался URL с /inventory.html, получен: {current_url}"
            print("✓ Успешный логин: перешли на страницу товаров")
    
    @allure.story("Неуспешная авторизация")
    @allure.title("Тест 2: Логин с неверным паролем")
    def test_invalid_password(self, login_page):
        """Тест логина с неверным паролем"""
        with allure.step("Ввод неверного пароля"):
            login_page.login(Config.VALID_USER, Config.INVALID_PASSWORD)
        
        with allure.step("Проверка сообщения об ошибке"):
            assert login_page.is_error_displayed(), "Сообщение об ошибке не отображается"
            error_text = login_page.get_error_message()
            assert "Username and password do not match" in error_text, \
                f"Неверный текст ошибки: {error_text}"
            print("✓ Неверный пароль: получено правильное сообщение об ошибке")
    
    @allure.story("Неуспешная авторизация")
    @allure.title("Тест 3: Логин заблокированного пользователя")
    def test_locked_user(self, login_page):
        """Тест логина заблокированного пользователя"""
        with allure.step("Логин заблокированным пользователем"):
            login_page.login(Config.LOCKED_USER, Config.VALID_PASSWORD)
        
        with allure.step("Проверка ошибки блокировки"):
            assert login_page.is_error_displayed(), "Сообщение об ошибке не отображается"
            error_text = login_page.get_error_message()
            assert "Sorry, this user has been locked out" in error_text, \
                f"Неверный текст ошибки: {error_text}"
            print("✓ Заблокированный пользователь: получено правильное сообщение")
    
    @allure.story("Неуспешная авторизация")
    @allure.title("Тест 4: Логин с пустыми полями")
    def test_empty_fields(self, login_page):
        """Тест логина с пустыми полями"""
        with allure.step("Нажатие Login без ввода данных"):
            login_page.click_login()
        
        with allure.step("Проверка валидации пустых полей"):
            assert login_page.is_error_displayed(), "Сообщение об ошибке не отображается"
            error_text = login_page.get_error_message()
            assert "Username is required" in error_text, \
                f"Неверный текст ошибки: {error_text}"
            print("✓ Пустые поля: получено правильное сообщение об ошибке")
    
    @allure.story("Успешная авторизация")
    @allure.title("Тест 5: Логин пользователем performance_glitch_user")
    def test_performance_user(self, login_page):
        """Тест логина пользователя с возможными задержками"""
        with allure.step("Логин пользователем с задержками"):
            login_page.login(Config.PERFORMANCE_USER, Config.VALID_PASSWORD)
            time.sleep(5)
        
        with allure.step("Проверка загрузки страницы"):
            current_url = login_page.driver.current_url
            assert "/inventory.html" in current_url, \
                f"Ожидался URL с /inventory.html, получен: {current_url}"
            print("✓ Пользователь с задержками: страница загрузилась успешно")