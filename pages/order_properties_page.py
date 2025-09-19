import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderPropertiesPage(BasePage):
    _CONTAINER_LOCATOR = (By.CSS_SELECTOR, "[class*='modal_opened']")

    @allure.step("Проверяем, что открыто модальное окно свойств заказа")
    def check_is_present(self):
        return self.get_element(*self._CONTAINER_LOCATOR).is_displayed()
