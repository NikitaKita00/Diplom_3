import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By


class OrderNewPage(BasePage):
    '''Окно (модальное) увдомления о создании нового заказа'''

    @property
    def close_button(self):
        return self.get_element(By.XPATH, "//section[contains(@class, 'modal_opened')]" 
                                          + "//button[contains(@class, 'close')]")
    @property
    def order_id(self):
        return int(self.get_element(By.XPATH, "//h2[contains(@class, 'text_type_digits-large')"
                " and not(.='9999')]").text)  
