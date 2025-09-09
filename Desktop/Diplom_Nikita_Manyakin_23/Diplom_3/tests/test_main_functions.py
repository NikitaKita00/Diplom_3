import allure
from .data import BUN_1, FILLING1_1, SAUCE_1
from .helper import register_and_login
from pages.account_page import AccounttPage
from pages.constructor_page import ConstructorPage
from pages.ingredient_properties_page import IngredientPropertiesPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage


class TestMainFunctions:
    @allure.title("Закрытие свойств ингредиента")
    @allure.description("Проверка закрытия свойств ингредиента по кнопке закрытия")
    def test_close_ingredient_properties(self, driver):
        MainPage().open()
        constructor_page = ConstructorPage()
        constructor_page.ingredient(BUN_1).click()
        ingredient_properties_page = IngredientPropertiesPage()
        ingredient_properties_page.check_is_present()
        ingredient_properties_page.close_button.click()
        assert ingredient_properties_page.check_is_hidden()

    @allure.title("Увеличение счётчика ингредиента")
    @allure.description("Проверка увеличения счётчика при добавлении ингредиента")
    def test_ingredient_counter_increase(self, driver):
        ingredient_name = FILLING1_1
        main_page = MainPage()
        main_page.open()
        constructor_page = ConstructorPage()
        count_before = constructor_page.ingredient_count(ingredient_name)
        constructor_page.add_ingredient(ingredient_name)
        count_after = constructor_page.ingredient_count(ingredient_name)
        assert count_before == 0 and count_after == 1

    @allure.title("Переход в конструктор")
    @allure.description("Проверка перехода с главной страницы в конструктор")
    def test_goto_constructor(self, driver):
        main_page = MainPage()
        main_page.open()
        main_page.cabinet_button.click()
        cabinet_page = AccounttPage()
        cabinet_page.check_is_present_and_not_logged()
        main_page.constructor_button.click()
        constructor_page = ConstructorPage()
        assert constructor_page.check_is_present()

    @allure.title("Переход в свойства ингредиента")
    @allure.description("Переход к свойствам ингредиента по клику")
    def test_goto_ingredient_properties(self, driver):
        MainPage().open()
        constructor_page = ConstructorPage()
        constructor_page.ingredient(BUN_1).click()
        ingredient_properties_page = IngredientPropertiesPage()
        assert ingredient_properties_page.check_is_present()

    @allure.title("Переход в ленту заказов")
    @allure.description("Переход с главной страницы в ленту заказов (ЛК)")
    def test_goto_orders(self, driver):
        main_page = MainPage()
        main_page.open()
        main_page.orders_button.click()
        orders_page = OrdersPage()
        assert orders_page.check_is_present()

    @allure.title("Доступность оформления заказа")
    @allure.description("Проверка, что залогиненный пользователь может оформить заказ")
    def test_order_creation_enabled(self, driver):
        register_and_login()
        constructor_page = ConstructorPage()
        constructor_page.add_ingredient(BUN_1)
        constructor_page.add_ingredient(SAUCE_1)
        constructor_page.add_ingredient(FILLING1_1)
        assert constructor_page.order_create_button
