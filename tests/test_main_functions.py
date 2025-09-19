import allure
from data import BUN_1, FILLING1_1, SAUCE_1
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from pages.ingredient_properties_page import IngredientPropertiesPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage


class TestMainFunctions:
    @allure.title("Закрытие свойств ингредиента")
    @allure.description("Проверка закрытия свойств ингредиента по кнопке закрытия")
    def test_close_ingredient_properties(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        constructor_page = ConstructorPage(driver)
        ingredient_properties_page = constructor_page.open_ingredient_properties(BUN_1)
        assert ingredient_properties_page.check_is_present()
        ingredient_properties_page.close()
        assert ingredient_properties_page.check_is_hidden()

    @allure.title("Клик по ингредиенту")
    @allure.description("Проверка что можно кликнуть по ингредиенту (упрощенная версия)")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        ingredient_name = FILLING1_1
        constructor_page = ConstructorPage(driver)
        assert constructor_page.is_ingredient_visible(ingredient_name), "Ingredient is not visible"
        count_before = constructor_page.ingredient_count(ingredient_name)
        constructor_page.click_ingredient(ingredient_name)
        assert constructor_page.ingredient_count(ingredient_name) > count_before

    @allure.title("Переход в конструктор")
    @allure.description("Проверка перехода с главной страницы в конструктор")
    def test_goto_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_account()
        account_page = AccountPage(driver)
        assert account_page.check_is_present_and_not_logged()
        main_page.go_to_constructor()
        constructor_page = ConstructorPage(driver)
        assert constructor_page.check_is_present()

    @allure.title("Переход в свойства ингредиента")
    @allure.description("Переход к свойствам ингредиента по клику")
    def test_goto_ingredient_properties(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        constructor_page = ConstructorPage(driver)
        ingredient_properties_page = constructor_page.open_ingredient_properties(BUN_1)
        assert ingredient_properties_page.check_is_present()

    @allure.title("Переход в ленту заказов")
    @allure.description("Переход с главной страницы в ленту заказов (ЛК)")
    def test_goto_orders(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_orders()
        orders_page = OrdersPage(driver)
        assert orders_page.check_is_present()

    @allure.title("Доступность оформления заказа")
    @allure.description("Проверка, что залогиненный пользователь может оформить заказ")
    def test_order_creation_enabled(self, logged_in_driver):
        driver = logged_in_driver
        main_page = MainPage(driver)
        main_page.open()
        
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient(BUN_1)
        constructor_page.add_ingredient(SAUCE_1)
        constructor_page.add_ingredient(FILLING1_1)
        assert constructor_page.is_order_creation_enabled()
