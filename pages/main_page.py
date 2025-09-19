import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from data import SITE_URL


class MainPage(BasePage):
    _CABINET_BUTTON_LOCATOR = (By.LINK_TEXT, "Личный Кабинет")
    _CONSTRUCTOR_BUTTON_LOCATOR = (By.LINK_TEXT, "Конструктор")
    _ORDERS_BUTTON_LOCATOR = (By.LINK_TEXT, "Лента Заказов")

    @property
    def cabinet_button(self):
        return self.get_element(*self._CABINET_BUTTON_LOCATOR)

    @property
    def constructor_button(self):
        return self.get_element(*self._CONSTRUCTOR_BUTTON_LOCATOR)

    @property
    def orders_button(self):
        return self.get_element(*self._ORDERS_BUTTON_LOCATOR)

    @allure.step("Открываем главную страницу")
    def open(self):
        self.open_url(SITE_URL)

    @allure.step("Переходим в личный кабинет")
    def go_to_account(self):
        self.safe_click(self.cabinet_button)

    @allure.step("Переходим в конструктор")
    def go_to_constructor(self):
        self.safe_click(self.constructor_button)

    @allure.step("Переходим в ленту заказов")
    def go_to_orders(self):
        self.safe_click(self.orders_button)
