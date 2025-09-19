import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from .base_page import BasePage


class IngredientPropertiesPage(BasePage):
    _TITLE_LOCATOR = (By.XPATH, "//h2[text()='Детали ингредиента']")
    _CLOSE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[class*='Modal_modal__close']")

    @property
    def close_button(self):
        return self.get_element(*self._CLOSE_BUTTON_LOCATOR)

    @allure.step("Закрываем модальное окно свойств ингредиента")
    def close(self):
        self.safe_click(self.close_button)

    @allure.step("Проверяем, что модальное окно с деталями ингредиента открыто")
    def check_is_present(self):
        return self.get_element(*self._TITLE_LOCATOR).is_displayed()

    @allure.step("Проверяем, что модальное окно закрыто")
    def check_is_hidden(self):
        return self.get_element(*self._TITLE_LOCATOR, condition=ec.invisibility_of_element_located)
