import allure
import pytest
import sys
import os
import time

# Добавляем корневую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from utils.data import TestData


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля через Личный Кабинет")
    def test_go_to_password_recovery(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_site()
        time.sleep(2)  # Ждем загрузки страницы

        main_page.click_personal_account()  # Нажимаем "Личный Кабинет"

        # Должны перейти на страницу логина
        assert login_page.is_login_page(), "Не удалось перейти на страницу входа"

        # Нажимаем "Восстановить пароль"
        login_page.go_to_forgot_password()

        forgot_page = ForgotPasswordPage(driver)
        assert (
            forgot_page.is_password_recovery_page()
        ), "Не удалось перейти на страницу восстановления пароля"
        assert (
            forgot_page.is_email_input_visible()
        ), "Поле ввода email не отображается на странице восстановления"

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_email_input_and_recovery(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_site()
        time.sleep(2)

        main_page.click_personal_account()  # Нажимаем "Личный Кабинет"

        # Должны перейти на страницу логина
        assert login_page.is_login_page(), "Не удалось перейти на страницу входа"

        # Нажимаем "Восстановить пароль"
        login_page.go_to_forgot_password()

        forgot_page = ForgotPasswordPage(driver)
        forgot_page.enter_email(TestData.EMAIL)
        forgot_page.click_recover_button()

        # После восстановления должны вернуться на страницу входа
        assert (
            login_page.is_login_page()
        ), "Не удалось перейти на страницу входа после восстановления"

    @allure.title("Кнопка 'Отмена' возвращает на страницу входа")
    def test_cancel_button_returns_to_login(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_site()
        time.sleep(2)

        main_page.click_personal_account()  # Нажимаем "Личный Кабинет"

        # Должны перейти на страницу логина
        assert login_page.is_login_page(), "Не удалось перейти на страницу входа"

        # Нажимаем "Восстановить пароль"
        login_page.go_to_forgot_password()

        forgot_page = ForgotPasswordPage(driver)
        forgot_page.click_cancel_button()

        assert (
            login_page.is_login_page()
        ), "Кнопка 'Отмена' не возвращает на страницу входа"
