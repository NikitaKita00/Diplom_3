from .base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators()

    def login(self, email, password):
        self.send_keys(self.locators.EMAIL_INPUT, email)
        self.send_keys(self.locators.PASSWORD_INPUT, password)
        self.click(self.locators.LOGIN_BUTTON)

    def login_with_detailed_locators(self, email, password):
        """Логин с использованием конкретных локаторов"""
        self.send_keys(self.locators.EMAIL_FIELD, email)
        self.send_keys(self.locators.PASSWORD_FIELD, password)
        self.click(self.locators.LOGIN_SUBMIT_BUTTON)

    def go_to_registration(self):
        self.click(self.locators.REGISTER_LINK)

    def go_to_forgot_password(self):
        self.click(self.locators.FORGOT_PASSWORD_LINK)
        self.wait_for_url_contains("forgot-password")

    def is_login_page(self):
        return "login" in self.driver.current_url and self.is_element_visible(
            self.locators.LOGIN_BUTTON
        )

    def is_login_successful(self):
        """Проверяем, что после логина мы на главной странице"""
        return (
            "stellarburgers" in self.driver.current_url
            and not "login" in self.driver.current_url
        )
