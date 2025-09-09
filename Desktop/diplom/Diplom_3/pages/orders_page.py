from .base_page import BasePage
from selenium.webdriver.common.by import By


class OrdersPage(BasePage):
    '''Лента заказов'''

    def order_by_id(self, id):
        return self.get_element(By.PARTIAL_LINK_TEXT, f"#{id:07d}")

    def order_in_progress_list(self, order_id):
        return self.get_element(By.XPATH, f"//ul[contains(@class, '_orderListReady_')]"
                                          f"/li[.='{order_id:07d}']")

    @property
    def order_last(self):
        return self.get_element(By.XPATH, "//*[contains(@class, 'OrderHistory_link_')][1]")

    @property
    def orders_today(self):
        return int(self.get_element(By.XPATH, "//*[.='Выполнено за сегодня:']/parent::*"
                                              "//*[contains(@class, '_number_')]").text)

    @property
    def orders_total(self):
        return int(self.get_element(By.XPATH, "//*[.='Выполнено за все время:']/parent::*"
                                              "//*[contains(@class, '_number_')]").text)

    @property
    def title(self):
        return self.get_element(By.XPATH, "//h1[normalize-space()='Лента заказов']")

    def check_is_present(self):
        return self.title