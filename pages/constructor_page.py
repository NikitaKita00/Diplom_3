from .base_page import BasePage
from locators.constructor_locators import ConstructorLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time


class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ConstructorLocators()

    def click_constructor(self):
        self.click(self.locators.CONSTRUCTOR_BUTTON)
        time.sleep(2)

    def click_order_feed(self):
        self.click(self.locators.ORDER_FEED_BUTTON)
        time.sleep(2)

    def click_ingredient(self):
        self.click(self.locators.INGREDIENT_ITEM)
        time.sleep(2)

    def close_modal(self):
        """Закрытие модального окна с обработкой исключений"""
        try:
            # Пробуем кликнуть по крестику
            close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.locators.MODAL_CLOSE_BUTTON)
            )
            close_button.click()
        except ElementClickInterceptedException:
            # Если крестик перекрыт, используем ESC
            from selenium.webdriver.common.keys import Keys

            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
        except:
            # Если все else fails, пробуем кликнуть по overlay через JS
            try:
                overlay = self.find_element(self.locators.MODAL_OVERLAY)
                self.driver.execute_script("arguments[0].click();", overlay)
            except:
                pass
        time.sleep(1)

    def close_modal_with_esc(self):
        """Закрытие модального окна клавишей ESC"""
        from selenium.webdriver.common.keys import Keys

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(1)

    def wait_for_modal_visible(self, timeout=5):
        """Ожидание появления модального окна"""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.locators.MODAL_WINDOW)
        )

    def wait_for_modal_hidden(self, timeout=5):
        """Ожидание скрытия модального окна"""
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(self.locators.MODAL_WINDOW)
        )

    def drag_ingredient_to_constructor(self):
        """Перетаскивание ингредиента в конструктор - исправленная версия"""
        try:
            source_element = self.find_element(self.locators.DRAGGABLE_INGREDIENT)
            target_element = self.find_element(self.locators.BURGER_CONSTRUCTOR)

            # Используем ActionChains для точного drag and drop
            actions = ActionChains(self.driver)

            # Вариант 1: Простое перетаскивание
            actions.drag_and_drop(source_element, target_element).perform()

            # Вариант 2: Более точное перетаскивание с offset
            # actions.click_and_hold(source_element).pause(1).move_to_element(target_element).pause(1).release().perform()

            time.sleep(2)

        except Exception as e:
            print(f"Ошибка при перетаскивании: {e}")
            # Fallback: кликаем на ингредиент и потом на конструктор
            try:
                source_element.click()
                time.sleep(1)
                target_element.click()
                time.sleep(1)
            except:
                pass

    def drag_ingredient_with_offset(self):
        """Перетаскивание с указанием точных координат"""
        try:
            source_element = self.find_element(self.locators.DRAGGABLE_INGREDIENT)
            constructor_section = self.find_element(
                (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")
            )

            # Получаем координаты целевой области
            target_location = constructor_section.location
            target_size = constructor_section.size

            # Вычисляем центр целевой области
            target_x = target_location["x"] + target_size["width"] // 2
            target_y = target_location["y"] + target_size["height"] // 2

            actions = ActionChains(self.driver)
            actions.click_and_hold(source_element).pause(0.5)
            actions.move_by_offset(target_x, target_y).pause(0.5)
            actions.release().perform()

            time.sleep(2)

        except Exception as e:
            print(f"Ошибка при перетаскивании с offset: {e}")

    def get_ingredient_counter(self, element):
        """Получение значения каунтера ингредиента"""
        try:
            counter = element.find_element(*self.locators.INGREDIENT_COUNTER)
            return int(counter.text) if counter.text else 0
        except:
            return 0

    def make_order(self):
        self.click(self.locators.ORDER_BUTTON)
        time.sleep(3)

    def is_modal_visible(self):
        return self.is_element_visible(self.locators.MODAL_WINDOW)

    def is_order_modal_visible(self):
        return self.is_element_visible(self.locators.ORDER_MODAL)

    def is_constructor_page(self):
        return self.is_element_visible(self.locators.BURGER_CONSTRUCTOR)

    def get_order_total(self):
        try:
            element = self.find_element(self.locators.ORDER_TOTAL)
            return element.text if element else "0"
        except:
            return "0"
