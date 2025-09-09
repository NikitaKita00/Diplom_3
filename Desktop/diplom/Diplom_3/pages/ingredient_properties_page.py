from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class IngredientPropertiesPage(BasePage):
    '''Модальное окно свойств ингредиента'''

    _TITLE_LOCATOR = (By.XPATH, "//h2[normalize-space()='Детали ингредиента']")

    @property
    def close_button(self):
        return self.get_element(By.XPATH, "//section[contains(@class, 'modal_opened')]"  # иначе найдёт 2 кнопки
                                          + "//button[contains(@class, 'close')]")

    @property
    def title(self):
        return self.get_element(*self._TITLE_LOCATOR)

    def check_is_present(self):
        return self.title

    def check_is_hidden(self):
        return self.get_element(*self._TITLE_LOCATOR, expected_condition=ec.invisibility_of_element_located)
            