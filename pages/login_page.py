import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from data import SITE_URL


class LoginPage(BasePage):
    _LOGIN_INPUT_LOCATOR = (By.XPATH, "//input[@name='name']")
    _PASSWORD_INPUT_LOCATOR = (By.XPATH, "//input[@name='Пароль']")
    _LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Войти']")

    @allure.step("Открываем страницу входа")
    def open(self):
        self.open_url(f"{SITE_URL}/login")

    @allure.step("Выполняем вход с email {email}")
    def login(self, email: str, password: str):
        email_input = self.get_element(*self._LOGIN_INPUT_LOCATOR)
        email_input.clear()
        email_input.send_keys(email)
        
        password_input = self.get_element(*self._PASSWORD_INPUT_LOCATOR)
        password_input.clear()
        password_input.send_keys(password)
        
        self.safe_click(self.get_element(*self._LOGIN_BUTTON_LOCATOR))
