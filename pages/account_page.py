import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class AccountPage(BasePage):
    _ORDERS_LINK_LOCATOR = (By.LINK_TEXT, "История заказов")
    _LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(), 'Выход')]")
    _ORDERS_BOX_LOCATOR = (By.CSS_SELECTOR, "[class*='OrderHistory_orderHistory']")
    _ENTER_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(), 'Войти')]")
    _PASSWORD_RECOVER_LINK_LOCATOR = (By.LINK_TEXT, "Восстановить пароль")

    @allure.step("Проверяем, что пользователь авторизован")
    def check_is_present_and_logged(self) -> bool:
        by, selector = self._LOGOUT_BUTTON_LOCATOR
        return self.wait_for_element_visibility(by, selector, timeout=2) is not None

    @allure.step("Проверяем, что пользователь не авторизован")
    def check_is_present_and_not_logged(self) -> bool:
        by, selector = self._ENTER_BUTTON_LOCATOR
        return self.wait_for_element_visibility(by, selector, timeout=2) is not None

    @allure.step("Кликаем по ссылке 'История заказов'")
    def click_orders_link(self) -> None:
        self.safe_click(self.get_element(*self._ORDERS_LINK_LOCATOR))

    @allure.step("Кликаем по кнопке 'Выход'")
    def click_logout_button(self) -> None:
        self.safe_click(self.get_element(*self._LOGOUT_BUTTON_LOCATOR))

    @allure.step("Проверяем отображение блока истории заказов")
    def is_orders_box_displayed(self) -> bool:
        by, selector = self._ORDERS_BOX_LOCATOR
        return self.wait_for_element_visibility(by, selector, timeout=2) is not None

    @allure.step("Переходим к восстановлению пароля")
    def go_to_password_recover(self) -> None:
        self.safe_click(self.get_element(*self._PASSWORD_RECOVER_LINK_LOCATOR))
