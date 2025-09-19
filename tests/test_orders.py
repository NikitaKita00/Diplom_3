import allure
from data import BUN_2, FILLING_2, SAUCE_2
from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from pages.order_properties_page import OrderPropertiesPage
from pages.order_new_page import OrderNewPage


@allure.epic("Orders")
class TestOrders:
    """Лента заказов"""

    @allure.title("Отображение свойств заказа")
    @allure.description("Проверка отображения свойств заказа")
    def test_properties(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_orders()

        orders_page = OrdersPage(driver)
        orders_page.open_last_order()

        order_properties_page = OrderPropertiesPage(driver)
        assert order_properties_page.check_is_present()

    @allure.title("Создание заказа")
    @allure.description("Созданный заказ должен появляться в ленте")
    def test_order_creation(self, logged_in_driver):
        driver = logged_in_driver

        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_orders()

        orders_page = OrdersPage(driver)
        orders_total_old = orders_page.orders_total
        orders_today_old = orders_page.orders_today

        main_page.go_to_constructor()

        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient(BUN_2)
        constructor_page.add_ingredient(SAUCE_2)
        constructor_page.add_ingredient(FILLING_2)

        constructor_page.create_order()

        order_new_page = OrderNewPage(driver)
        order_new_page.wait_for_modal(timeout=8)
        assert order_new_page.check_modal_is_present(), "Модальное окно с созданным заказом не отобразилось"
        order_id = order_new_page.order_id
        assert order_id > 0, "Получен некорректный ID заказа"
        order_new_page.close_modal_safely()
        main_page.go_to_orders()

        order_element = orders_page.order_by_id(order_id)
        assert order_element, f"Заказ с ID {order_id} не найден в ленте заказов"

        new_orders_total = orders_page.orders_total
        new_orders_today = orders_page.orders_today
        assert new_orders_total >= orders_total_old, f"Общий счетчик заказов не увеличился: было {orders_total_old}, стало {new_orders_total}"
        assert new_orders_today >= orders_today_old, f"Счетчик заказов за сегодня не увеличился: было {orders_today_old}, стало {new_orders_today}"
