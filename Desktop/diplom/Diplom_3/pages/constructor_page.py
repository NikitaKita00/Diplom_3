import allure
from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ConstructorPage(BasePage):
    '''Страница конструктора'''

    @property
    def burger(self):
        return self.get_element(By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket_')]")

    def check_is_present(self):
        return self.title

    @property
    def order_create_button(self):
        return self.get_element(By.XPATH, "//button[normalize-space()='Оформить заказ']")

    @property
    def title(self):
        return self.get_element(By.XPATH, "//h1[normalize-space()='Соберите бургер']")

    @allure.step('Добавление ингредиента в бургер')
    def add_ingredient(self, name):
        ingredient = self.ingredient(name)
        ac = ActionChains(self._driver)
        ac.scroll_to_element(ingredient)
        ac.drag_and_drop(ingredient, self.burger)
        ac.perform()

    def _get_ingredient_xpath(self, name):
        return f"//*[contains(@class, '_ingredient_') and normalize-space()='{name}']/parent::*"

    def ingredient(self, name):
        return self.get_element(By.XPATH, self._get_ingredient_xpath(name))

    def ingredient_count(self, name):
        text = self.get_element(By.XPATH, self._get_ingredient_xpath(name)
            + "//*[contains(@class, '_counter__num_')]").text
        return int(text)
