# pages/login_page.py
from selenium.webdriver.common.by import By
import allure
from utils.config import Config


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(Config.BASE_URL)
    
    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    @allure.step("Ввод логина: {username}")
    def enter_username(self, username):
        element = self.driver.find_element(*self.USERNAME_INPUT)
        element.clear()
        element.send_keys(username)
        return self
    
    @allure.step("Ввод пароля: {password}")
    def enter_password(self, password):
        element = self.driver.find_element(*self.PASSWORD_INPUT)
        element.clear()
        element.send_keys(password)
        return self
    
    @allure.step("Нажатие кнопки Login")
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self
    
    @allure.step("Логин с данными: {username}")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self
    
    @allure.step("Получение текста ошибки")
    def get_error_message(self):
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except:
            return ""
    
    @allure.step("Проверка отображения ошибки")
    def is_error_displayed(self):
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).is_displayed()
        except:
            return False