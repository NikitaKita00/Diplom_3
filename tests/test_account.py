import allure
import pytest
from pages.main_page import MainPage
from pages.account_page import AccountPage


@pytest.mark.usefixtures("driver")
class TestUserAccount:
    """Набор тестов для проверки личного кабинета"""

    @allure.title("Открытие раздела личного кабинета")
    @allure.description("Тест перехода с главной страницы в личный кабинет")
    def test_access_account_section(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_account()
        account_page = AccountPage(driver)
        assert account_page.check_is_present_and_not_logged()

    @allure.title("Просмотр истории заказов")
    @allure.description("Тест перехода от личного кабинета к истории заказов (упрощенная версия)")
    def test_view_order_history(self, logged_in_driver):
        driver = logged_in_driver
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_account()
        
        account_page = AccountPage(driver)
        account_page.click_orders_link()
        assert account_page.is_orders_box_displayed(), "История заказов не отображается"
    @allure.title("Выход из аккаунта")
    @allure.description("Проверка выхода из аккаунта для авторизованного пользователя (упрощенная версия)")
    def test_user_logout(self, logged_in_driver):
        driver = logged_in_driver
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_account()
        
        account_page = AccountPage(driver)
        account_page.click_logout_button()
        assert account_page.check_is_present_and_not_logged(), "Пользователь не вышел из аккаунта"
