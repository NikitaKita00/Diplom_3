import allure
from .data import BUN_2, FILLING_2, SAUCE_2
from .helper import register_and_login
from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from pages.order_properties_page import OrderPropertiesPage
from pages.order_new_page import OrderNewPage


class TestOrders:
    '''Лента заказов'''

    @allure.title('Отображение заказов')
    @allure.description('Отображения свойств заказа')
    def test_properties(self, driver):
        main_page = MainPage()
        main_page.open()
        main_page.orders_button.click()
        orders_page = OrdersPage()
        orders_page.order_last.click()
        order_properties_page = OrderPropertiesPage()
        assert order_properties_page.check_is_present()

    @allure.title('Созданние заказа')
    @allure.description('Созданный заказ должен появился в ленте')
    def test_order_creation(self, driver):
        register_and_login()
        main_page = MainPage()
        main_page.orders_button.click()
        orders_page = OrdersPage()
        orders_total_old = orders_page.orders_total
        orders_today_old = orders_page.orders_today
        main_page.constructor_button.click()
        constructor_page = ConstructorPage()
        constructor_page.add_ingredient(BUN_2)
        constructor_page.add_ingredient(SAUCE_2)
        constructor_page.add_ingredient(FILLING_2)
        constructor_page.order_create_button.click()
        order_new_page = OrderNewPage()
        order_id = order_new_page.order_id
        order_new_page.close_button.click()
        main_page.orders_button.click()
        assert orders_page.order_by_id(order_id) \
               and orders_page.orders_total == orders_total_old + 1 \
               and orders_page.orders_today == orders_today_old + 1 \
               and orders_page.order_in_progress_list(order_id)
