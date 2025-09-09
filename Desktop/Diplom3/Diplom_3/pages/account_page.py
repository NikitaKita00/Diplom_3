from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class AccounttPage(BasePage):
    """Страница личного кабинета"""

    _INPUT_BY_LABEL_XPATH_PATTERN = "//label[.='{label}']/parent::*//input"
    _EMAIL_LOCATOR = (By.XPATH, _INPUT_BY_LABEL_XPATH_PATTERN.format(label="Email"))
    _PASSWORD_LOCATOR = (By.XPATH, _INPUT_BY_LABEL_XPATH_PATTERN.format(label="Пароль"))

    @property
    def email(self):
        return self.get_input_value(self._EMAIL_LOCATOR)

    def set_email(self, value):
        self.set_input_value(self._EMAIL_LOCATOR, value)

    @property
    def enter_button(self):
        return self.get_element(By.XPATH, "//button[.='Войти']")

    @property
    def logout_button(self):
        return self.get_element(By.XPATH, "//button[.='Выход']")

    @property
    def orders_box(self):
        return self.get_element(
            By.XPATH,
            "//*[contains(@class, 'OrderHistory_orderHistory')]",
            expected_condition=ec.presence_of_element_located,
        )

    @property
    def orders_link(self):
        return self.get_element(By.LINK_TEXT, "История заказов")

    @property
    def password(self):
        return self.get_input_value(self._PASSWORD_LOCATOR)

    def set_password(self, value):
        self.set_input_value(self._PASSWORD_LOCATOR, value)

    @property
    def password_recover_link(self):
        return self.get_element(By.LINK_TEXT, "Восстановить пароль")

    @property
    def register_link(self):
        return self.get_element(By.LINK_TEXT, "Зарегистрироваться")

    def check_is_present_and_logged(self):
        self.logout_button
        return True

    def check_is_present_and_not_logged(self):
        self.enter_button
        return True

    def login(self, email, password):
        self.check_is_present_and_not_logged()
        self.set_email(email)
        self.set_password(password)
        self.enter_button.click()
