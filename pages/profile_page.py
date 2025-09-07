from .base_page import BasePage
from locators.profile_locators import ProfileLocators
import time


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProfileLocators()

    def go_to_order_history(self):
        self.click(self.locators.ORDER_HISTORY_LINK)
        self.wait_for_url_contains("order-history")

    def logout(self):
        """Выход из аккаунта с обработкой возможных проблем"""
        # Закрываем модальные окна, если есть
        self.close_modal_if_present()

        # Ждем немного перед кликом
        time.sleep(2)

        # Пробуем разные способы клика
        try:
            # Способ 1: Обычный клик
            self.click(self.locators.LOGOUT_BUTTON)
        except:
            try:
                # Способ 2: Альтернативный локатор
                self.click(self.locators.LOGOUT_BUTTON_ALT)
            except:
                try:

                    element = self.find_element(self.locators.LOGOUT_BUTTON)
                    self.driver.execute_script("arguments[0].click();", element)
                except:
                    # Способ 4: Поиск по тексту
                    logout_buttons = self.driver.find_elements(
                        By.XPATH, "//button[contains(text(), 'Выход')]"
                    )
                    if logout_buttons:
                        self.driver.execute_script(
                            "arguments[0].click();", logout_buttons[0]
                        )
                    else:
                        raise Exception("Не удалось найти кнопку выхода")

        # Ждем перехода на страницу входа
        self.wait_for_url_contains("login")
        time.sleep(2)

    def click_personal_account(self):
        self.click(self.locators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_for_url_contains("profile")
        time.sleep(2)

    def is_profile_page(self):
        return "profile" in self.driver.current_url and self.is_element_visible(
            self.locators.PROFILE_SECTION
        )

    def is_order_history_page(self):
        return "order-history" in self.driver.current_url and self.is_element_visible(
            self.locators.ORDER_HISTORY_LINK
        )

    def get_profile_info(self):
        """Получаем информацию из полей профиля"""
        name = self.find_element(self.locators.NAME_INPUT).get_attribute("value")
        email = self.find_element(self.locators.EMAIL_INPUT).get_attribute("value")
        return {"name": name, "email": email}

    def update_profile(self, name=None, email=None, password=None):
        if name:
            name_input = self.find_element(self.locators.NAME_INPUT)
            name_input.clear()
            name_input.send_keys(name)

        if email:
            email_input = self.find_element(self.locators.EMAIL_INPUT)
            email_input.clear()
            email_input.send_keys(email)

        if password:
            password_input = self.find_element(self.locators.PASSWORD_INPUT)
            password_input.clear()
            password_input.send_keys(password)

        self.click(self.locators.SAVE_BUTTON)
        time.sleep(1)
