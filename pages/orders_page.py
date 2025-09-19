import re

import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class OrdersPage(BasePage):
    _ORDER_LINKS_LOCATOR = (By.CSS_SELECTOR, "[class*='OrderHistory_link']")
    _ORDERS_TODAY_LOCATOR = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    _ORDERS_TOTAL_LOCATOR = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    _TITLE_LOCATOR = (By.XPATH, "//h1[text()='Лента заказов']")

    _ORDER_LINK_BY_ID_XPATH_TEMPLATE = "//a[contains(., '#{order_id}')]"
    _ORDER_IN_PROGRESS_ID_XPATH_TEMPLATE = "//ul[contains(@class, 'orderListReady')]/li[text()='{order_id}']"

    @allure.step("Получаем заказ по ID {order_id}")
    def order_by_id(self, order_id):
        locator = (By.XPATH, self._ORDER_LINK_BY_ID_XPATH_TEMPLATE.format(order_id=order_id))
        return self.get_element(*locator)

    @allure.step("Получаем заказ {order_id} из списка в работе")
    def order_in_progress_list(self, order_id):
        locator = (By.XPATH, self._ORDER_IN_PROGRESS_ID_XPATH_TEMPLATE.format(order_id=order_id))
        return self.get_element(*locator)

    @property
    def order_last(self):
        elements = self.find_elements(*self._ORDER_LINKS_LOCATOR)
        return elements[0] if elements else None

    @allure.step("Открываем первый заказ в ленте")
    def open_last_order(self) -> None:
        el = self.order_last
        assert el is not None, "Лента заказов пуста"
        self.safe_click(el)

    def _extract_number_from_element(self, locator):
        """Вспомогательный метод для извлечения числа из элемента"""
        try:
            element = self.get_element(*locator)
            text = element.text.strip()
            numbers = re.findall(r'\d+', text)
            if numbers:
                return int(numbers[0])
        except:
            pass
        return 0

    @property
    def orders_today(self):
        return self._extract_number_from_element(self._ORDERS_TODAY_LOCATOR)

    @property
    def orders_total(self):
        return self._extract_number_from_element(self._ORDERS_TOTAL_LOCATOR)

    @allure.step("Проверяем, что страница ленты заказов загружена")
    def check_is_present(self):
        return self.get_element(*self._TITLE_LOCATOR).is_displayed()
