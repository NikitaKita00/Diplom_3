import allure
from .helper import register_and_login
from pages.account_page import AccounttPage
from pages.main_page import MainPage


class TestUserAccount:
    """Набор тестов для проверки личного кабинета"""

    @allure.step("Открываем личный кабинет")
    def _open_account_page(self):
        MainPage().cabinet_button.click()
        cabinet = AccounttPage()
        cabinet.check_is_present_and_logged()
        return cabinet

    @allure.title("Открытие раздела личного кабинета")
    @allure.description("Тест перехода с главной страницы в личный кабинет")
    def test_access_account_section(self, driver):
        main = MainPage()
        main.open()
        main.cabinet_button.click()
        cabinet = AccounttPage()
        assert cabinet.check_is_present_and_not_logged()

    @allure.title("Просмотр истории заказов")
    @allure.description("Тест перехода от личного кабинета к истории заказов")
    def test_view_order_history(self, driver):
        register_and_login()
        cabinet = self._open_account_page()
        cabinet.orders_link.click()
        assert cabinet.orders_box is not None

    @allure.title("Выход из аккаунта")
    @allure.description("Проверка выхода из аккаунта для авторизованного пользователя")
    def test_user_logout(self, driver):
        register_and_login()
        cabinet = self._open_account_page()
        cabinet.logout_button.click()
        assert cabinet.check_is_present_and_not_logged()
