import re

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from .base_page import BasePage


class OrderNewPage(BasePage):
    _ORDER_ID_LOCATOR = (By.CSS_SELECTOR, "[class*='Modal_modal__title']")
    _CLOSE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[class*='Modal_modal__close']")
    _BODY_LOCATOR = (By.TAG_NAME, "body")

    @allure.step("Получаем ID созданного заказа")
    def get_order_id(self):
        element = self.get_element(*self._ORDER_ID_LOCATOR)
        text = element.text or ""
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else 0

    @property
    def order_id(self):
        """Свойство для обратной совместимости"""
        return self.get_order_id()

    @allure.step("Получаем кнопку закрытия модального окна заказа")
    def get_close_button(self):
        return self.get_element(*self._CLOSE_BUTTON_LOCATOR)

    @property
    def close_button(self):
        """Свойство для обратной совместимости"""
        return self.get_close_button()

    @allure.step("Закрываем модальное окно нового заказа")
    def close_modal(self):
        close_btn = self.get_close_button()
        self.safe_click(close_btn)

    @allure.step("Безопасно закрываем модальное окно нового заказа")
    def close_modal_safely(self):
        """Закрывает модальное окно с минимальным фолбэком без локаторов в методах"""
        try:
            self.close_modal()
        except Exception:
            try:
                body = self.find_element_safe(*self._BODY_LOCATOR, timeout=2)
                if body:
                    body.send_keys(Keys.ESCAPE)
            except Exception:
                pass

    @allure.step("Ждем появления модального окна с заказом")
    def wait_for_modal(self, timeout=8):
        """Ожидает появления модального окна с заказом"""
        WebDriverWait(self._driver, timeout).until(
            ec.visibility_of_element_located(self._ORDER_ID_LOCATOR)
        )

    @allure.step("Проверяем, что модальное окно с заказом отображается")
    def check_modal_is_present(self):
        el = self.find_element_safe(*self._ORDER_ID_LOCATOR, timeout=2)
        return bool(el and el.is_displayed())
