import allure
import pytest
import sys
import os
import time
from selenium.webdriver.common.by import By

# Добавляем корневую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestProfile:

    @pytest.fixture(autouse=True)
    def setup(self, driver, api_client):
        self.api_client = api_client
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)

        # Создаем пользователя через API
        self.user_data = self.api_client.create_user(
            "manya.nzenliv@gmail.com", "qwe123qwe", "Test User"
        )

        # Переходим на сайт
        self.main_page.go_to_site()
        time.sleep(3)

        # Логинимся
        self.main_page.click_personal_account()
        time.sleep(2)
        self.login_page.login_with_detailed_locators(
            "manya.nzenliv@gmail.com", "qwe123qwe"
        )
        time.sleep(3)

        yield

        # Удаляем пользователя после теста
        if "accessToken" in self.user_data:
            self.api_client.delete_user(self.user_data["accessToken"])

    @allure.title("Переход в личный кабинет")
    def test_go_to_profile(self, driver):
        """Проверка перехода в личный кабинет"""
        # Уже залогинены, переходим в профиль
        self.profile_page.click_personal_account()
        assert (
            self.profile_page.is_profile_page()
        ), "Не удалось перейти в личный кабинет"

    @allure.title("Переход в историю заказов")
    def test_go_to_order_history(self, driver):
        """Проверка перехода в историю заказов"""
        # Переходим в профиль
        self.profile_page.click_personal_account()
        assert (
            self.profile_page.is_profile_page()
        ), "Не удалось перейти в личный кабинет"

        # Переходим в историю заказов
        self.profile_page.go_to_order_history()
        assert (
            self.profile_page.is_order_history_page()
        ), "Не удалось перейти в историю заказов"
