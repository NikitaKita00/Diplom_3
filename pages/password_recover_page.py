import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class PasswordRecoverPage(BasePage):
    _TITLE_LOCATOR = (By.XPATH, "//h2[text()='Восстановление пароля']")
    _EMAIL_INPUT_LOCATOR = (By.CSS_SELECTOR, "input[type='text']")
    _RECOVER_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Восстановить']")
    _PASSWORD_BOX_LOCATOR = (By.CSS_SELECTOR, "[class*='input_status_active']")
    _EYE_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".input__icon-action")
    _SAVE_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Сохранить']")

    @allure.step("Вводим email {value} для восстановления пароля")
    def set_email(self, value):
        email_input = self.get_element(*self._EMAIL_INPUT_LOCATOR)
        email_input.clear()
        email_input.send_keys(value)

    @allure.step("Кликаем по кнопке 'Восстановить'")
    def click_recover(self):
        self.safe_click(self.get_element(*self._RECOVER_BUTTON_LOCATOR))

    @allure.step("Проверяем, что открыта стартовая страница восстановления")
    def check_start_page_is_present(self):
        return self.get_element(*self._TITLE_LOCATOR).is_displayed()

    @allure.step("Кликаем по иконке глаза")
    def click_eye_button(self):
        self.safe_click(self.get_element(*self._EYE_BUTTON_LOCATOR))

    @allure.step("Проверяем, что поле пароля активно")
    def check_password_box_is_active(self):
        return "input_status_active" in self.get_element(*self._PASSWORD_BOX_LOCATOR).get_attribute("class")

    @allure.step("Проверяем, что открыта страница сохранения пароля")
    def check_save_page_is_present(self):
        return self.get_element(*self._SAVE_BUTTON_LOCATOR).is_displayed()
