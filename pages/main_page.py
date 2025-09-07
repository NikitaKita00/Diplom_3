from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainLocators()

    def wait_for_main_page_load(self, timeout=10):
        """Явное ожидание загрузки главной страницы"""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.locators.LOGO)
        )

    def click_personal_account(self):
        """Клик по кнопке 'Личный кабинет' с обработкой перехвата"""
        try:
            self.click(self.locators.PERSONAL_ACCOUNT_BUTTON)
        except:

            self.driver.execute_script(
                "arguments[0].click();",
                self.find_element(self.locators.PERSONAL_ACCOUNT_BUTTON),
            )

        # Ждем перехода на страницу логина или профиля
        WebDriverWait(self.driver, 10).until(
            lambda driver: "login" in driver.current_url
            or "profile" in driver.current_url
        )

    def is_main_page(self):
        """Проверка, что находимся на главной странице"""
        current_url = self.driver.current_url
        return current_url == f"{self.base_url}/" and self.is_element_visible(
            self.locators.LOGO
        )
