from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, timeout=2):
        self._driver = driver
        self._timeout = timeout

    def open_url(self, url: str):
        self._driver.get(url)

    def get_element(self, by, selector, condition=ec.visibility_of_element_located):
        return wait(self._driver, self._timeout).until(condition((by, selector)))

    def find_element_safe(self, by, selector, timeout=1):
        """Безопасный поиск элемента без исключений"""
        try:
            return wait(self._driver, timeout).until(ec.presence_of_element_located((by, selector)))
        except TimeoutException:
            return None

    def safe_click(self, element):
        try:
            ActionChains(self._driver).move_to_element(element).perform()
            wait(self._driver, 1).until(ec.element_to_be_clickable(element))
            element.click()
        except (ElementClickInterceptedException, TimeoutException):
            try:
                ActionChains(self._driver).click(element).perform()
            except:
                element.click()

    def scroll_to_element(self, element):
        """Прокручиваем к элементу используя ActionChains"""
        ActionChains(self._driver).move_to_element(element).perform()


    def find_elements(self, by, selector):
        """Находим все элементы по локатору"""
        return self._driver.find_elements(by, selector)

    def wait_for_element_presence(self, by, selector, timeout=1):
        """Ожидаем появления элемента на странице"""
        try:
            return wait(self._driver, timeout).until(ec.presence_of_element_located((by, selector)))
        except TimeoutException:
            return None

    def wait_for_element_visibility(self, by, selector, timeout=1):
        """Ожидаем, что элемент станет видимым"""
        try:
            return wait(self._driver, timeout).until(ec.visibility_of_element_located((by, selector)))
        except TimeoutException:
            return None
