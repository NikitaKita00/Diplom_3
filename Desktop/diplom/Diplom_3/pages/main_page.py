from .base_page import BasePage
from data import SITE_URL
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    '''Главная страница (меню в верхней части экрана + контейнер для др.страниц)'''

    @property
    def cabinet_button(self):
        return self.get_element(By.LINK_TEXT, 'Личный Кабинет')

    @property
    def constructor_button(self):
        return self.get_element(By.LINK_TEXT, 'Конструктор')

    @property
    def orders_button(self):
        return self.get_element(By.LINK_TEXT, 'Лента Заказов')

    def open(self):
        self._driver.get(SITE_URL)

