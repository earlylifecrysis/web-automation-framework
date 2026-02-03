# pages/inventory_page.py
from selenium.webdriver.common.by import By
import allure


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
    
    # Локаторы
    APP_LOGO = (By.CLASS_NAME, "app_logo")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    
    @allure.step("Проверка загрузки страницы товаров")
    def verify_page_loaded(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/inventory.html")
        )
        return self
    
    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Проверка отображения логотипа")
    def is_logo_displayed(self):
        try:
            return self.driver.find_element(*self.APP_LOGO).is_displayed()
        except:
            return False