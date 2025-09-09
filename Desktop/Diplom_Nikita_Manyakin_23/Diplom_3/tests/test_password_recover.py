import pytest
import allure
from selenium import webdriver
from pages.account_page import AccounttPage
from pages.main_page import MainPage
from pages.password_recover_page import PasswordRecoverPage
from pages.base_page import BasePage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    BasePage.set_driver(driver)
    yield driver
    driver.quit()


class TestPasswordRecover:
    """Тесты восстановления пароля"""

    @allure.step("Переход с гл.стр. к 1-й стр. восстановления пароля")
    def _goto_password_recover_start_page(self):
        main_page = MainPage()
        main_page.open()
        main_page.cabinet_button.click()
        cabinet_page = AccounttPage()
        cabinet_page.password_recover_link.click()
        return PasswordRecoverPage()

    @allure.step("Переход с гл.стр. к последней стр. восстановления пароля")
    def _goto_password_recover_save_page(self):
        password_recover_start_page = self._goto_password_recover_start_page()
        password_recover_start_page.set_email("any_valid_mail@box.gu")
        password_recover_start_page.recover_button.click()
        return PasswordRecoverPage()

    @allure.title("Поле пароля выделено при нажатии на глаз")
    @allure.description(
        "После нажатия на глаз поле пароля должно быть выделено (яркой рамкой)"
    )
    def test_email_active_on_eye_click(self, driver):
        password_recover_save_page = self._goto_password_recover_save_page()
        password_recover_save_page.eye_button.click()
        assert password_recover_save_page.check_password_box_is_active()

    @allure.title("Переход на страницу восстановления пароля")
    @allure.description(
        "Проверка перехода с главной страницы на страницу восстановления (через ЛК)"
    )
    def test_goto_password_recover_start(self, driver):
        password_recover_start_page = self._goto_password_recover_start_page()
        assert password_recover_start_page.check_start_page_is_present()

    @allure.title("Ввод почты и проверка кнопки Восстановить")
    @allure.description(
        "Проверка перехода к стр. сохранения нов.пароля при его восстановлении"
    )
    def test_goto_password_recover_save(self, driver):
        password_recover_save_page = self._goto_password_recover_save_page()
        assert password_recover_save_page.check_save_page_is_present()
