from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class OrderPropertiesPage(BasePage):
    '''Модальное окно свойств заказа'''


    @property
    def container(self):
        return self.get_element(By.XPATH, "//section[contains(@class, '_modal_opened_')]")

    def check_is_present(self):
        return self.container
            