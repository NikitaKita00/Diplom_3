from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PasswordRecoverPage(BasePage):
    @property
    def title(self):
        return self.get_element(
            By.XPATH, "//h2[normalize-space()='Восстановление пароля']"
        )

    @property
    def email_input(self):
        return self.get_element(By.XPATH, "//label[.='Email']/parent::*//input")

    def set_email(self, value):
        self.email_input.clear()
        self.email_input.send_keys(value)

    @property
    def recover_button(self):
        return self.get_element(By.XPATH, "//button[.='Восстановить']")

    def click_recover(self):
        self.recover_button.click()

    def check_start_page_is_present(self):
        self.title
        self.recover_button
        return True

    @property
    def password_box(self):
        return self.get_element(By.XPATH, "//label[.='Пароль']/parent::*")

    @property
    def eye_button(self):
        return self.get_element(By.CSS_SELECTOR, ".input__icon-action")

    def check_password_box_is_active(self):
        class_attr = self.password_box.get_attribute("class")
        return "input_status_active" in class_attr

    @property
    def save_button(self):
        return self.get_element(By.XPATH, "//button[.='Сохранить']")

    def click_save(self):
        self.save_button.click()

    def check_save_page_is_present(self):
        self.title
        self.save_button
        return True
