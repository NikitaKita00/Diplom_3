import allure
from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.ingredient_properties_page import IngredientPropertiesPage


class ConstructorPage(BasePage):
    _BURGER_LOCATOR = (By.CSS_SELECTOR, "[class*='BurgerConstructor_basket']")
    _ORDER_CREATE_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    _TITLE_LOCATOR = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    _INGREDIENT_XPATH_TEMPLATE = "//p[text()='{name}']/ancestor::a"
    _INGREDIENT_IN_CONSTRUCTOR_XPATH_TEMPLATE = "//*[contains(@class, 'constructor')]//*[contains(text(), '{name}')]"
    _INGREDIENT_COUNT_XPATH_TEMPLATE = "//p[text()='{name}']/ancestor::*//span[contains(@class, 'counter')]"

    @property
    def burger(self):
        return self.get_element(*self._BURGER_LOCATOR)

    @allure.step("Проверяем, что страница конструктора загружена")
    def check_is_present(self):
        return self.get_element(*self._TITLE_LOCATOR)

    @property
    def order_create_button(self):
        return self.get_element(*self._ORDER_CREATE_BUTTON_LOCATOR)

    @allure.step("Добавляем ингредиент {name} в конструктор")
    def add_ingredient(self, name):
        ing_locator = (By.XPATH, self._INGREDIENT_XPATH_TEMPLATE.format(name=name))
        burger_locator = self._BURGER_LOCATOR
        ingredient = WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable(ing_locator))
        burger_constructor = WebDriverWait(self._driver, 5).until(EC.visibility_of_element_located(burger_locator))

        self.scroll_to_element(ingredient)
        try:
            ActionChains(self._driver).drag_and_drop(ingredient, burger_constructor).perform()
        except Exception:
            self.safe_click(ingredient)
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self._INGREDIENT_IN_CONSTRUCTOR_XPATH_TEMPLATE.format(name=name)))
        )
                
    def _drag_and_drop_method1(self, source, target):
        actions = ActionChains(self._driver)
        actions.click_and_hold(source)
        actions.move_to_element(target)
        actions.release()
        actions.perform()
        
    def _html5_drag_and_drop(self, source, target):
        """Замена HTML5 drag-and-drop на чистый Python через ActionChains"""
        actions = ActionChains(self._driver)
        actions.drag_and_drop(source, target)
        actions.perform()
        
    def _mouse_drag_and_drop(self, source, target):
        actions = ActionChains(self._driver)
        actions.move_to_element(source)
        actions.click_and_hold()
        actions.move_to_element(target)
        actions.release()
        actions.perform()

    @allure.step("Создаем заказ")
    def create_order(self):
        self.safe_click(self.order_create_button)

    def ingredient(self, name):
        locator = (By.XPATH, self._INGREDIENT_XPATH_TEMPLATE.format(name=name))
        return self.get_element(*locator)

    @allure.step("Проверяем, что ингредиент {name} добавлен в конструктор")
    def check_ingredient_in_constructor(self, name):
        """Проверяем, был ли ингредиент добавлен в конструктор"""
        locator = (By.XPATH, self._INGREDIENT_IN_CONSTRUCTOR_XPATH_TEMPLATE.format(name=name))
        element = self.find_element_safe(*locator, timeout=2)
        return element is not None

    @allure.step("Получаем количество ингредиента {name}")
    def ingredient_count(self, name):
        locator = (By.XPATH, self._INGREDIENT_COUNT_XPATH_TEMPLATE.format(name=name))
        element = self.find_element_safe(*locator, timeout=1)
        if not element:
            return 0
        text = (element.text or "").strip()
        return int(text) if text.isdigit() else 0

    @allure.step("Кликаем по ингредиенту {name}")
    def click_ingredient(self, name):
        """Высокоуровневый клик по ингредиенту без возврата WebElement в тест"""
        ingredient = self.ingredient(name)
        self.scroll_to_element(ingredient)
        self.safe_click(ingredient)

    @allure.step("Проверяем видимость ингредиента {name}")
    def is_ingredient_visible(self, name) -> bool:
        el = self.find_element_safe(By.XPATH, self._INGREDIENT_XPATH_TEMPLATE.format(name=name), timeout=2)
        return bool(el and el.is_displayed())

    @allure.step("Открываем свойства ингредиента {name}")
    def open_ingredient_properties(self, name) -> IngredientPropertiesPage:
        """Открывает модальное окно свойств ингредиента и возвращает объект страницы свойств"""
        self.click_ingredient(name)
        page = IngredientPropertiesPage(self._driver)
        return page

    @allure.step("Доступно ли оформление заказа")
    def is_order_creation_enabled(self) -> bool:
        try:
            btn = self.order_create_button
            return bool(btn and btn.is_enabled())
        except Exception:
            return False
