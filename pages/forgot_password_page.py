from .base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPasswordLocators()

    def enter_email(self, email):
        self.send_keys(self.locators.EMAIL_INPUT, email)

    def click_recover_button(self):
        self.click(self.locators.RECOVER_BUTTON)
        # Ждем перехода на страницу входа
        self.wait_for_url_contains("login")

    def click_show_password(self):
        self.click(self.locators.SHOW_PASSWORD_BUTTON)

    def click_cancel_button(self):
        self.click(self.locators.CANCEL_BUTTON)
        # Ждем перехода на страницу входа
        self.wait_for_url_contains("login")

    def is_password_field_active(self):
        return self.is_element_visible(self.locators.ACTIVE_PASSWORD_FIELD)

    def is_password_recovery_page(self):
        return "forgot-password" in self.driver.current_url

    def is_email_input_visible(self):
        return self.is_element_visible(self.locators.EMAIL_INPUT)
