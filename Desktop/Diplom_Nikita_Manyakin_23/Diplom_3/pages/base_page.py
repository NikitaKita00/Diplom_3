from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as wait


class BasePage:
    '''Базовая страница (для всех других страниц)'''
    
    _driver = None
    _timeout = 5

    @classmethod
    def set_driver(cls, driver):
        cls._driver = driver

    def get_element(self, by, selector, expected_condition = ec.visibility_of_element_located):
        return wait(self._driver, self._timeout).until(expected_condition((by, selector)))

    def get_input_value(self, locator):
        return self.get_element(*locator).get_attribute('value')

    def set_input_value(self, locator, value):
        return self.get_element(*locator).send_keys(value)
