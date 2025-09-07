import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test_simple_drag(driver):
    """Простой тест перетаскивания"""
    # Переходим на сайт
    driver.get("https://stellarburgers.nomoreparties.site")
    time.sleep(3)

    # Логинимся
    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
    time.sleep(2)


    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(
        "manya.nzenliv@gmail.com"
    )
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("qwe123qwe")
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    time.sleep(3)

    
    try:
        ingredient = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[1]/a[2]")
            )
        )
        print("Ингредиент найден!")

        constructor = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")
            )
        )
        print("Конструктор найден!")

        


        actions = ActionChains(driver)
        actions.drag_and_drop(ingredient, constructor).perform()
        time.sleep(2)

        print("Перетаскивание выполнено!")
        assert True

    except Exception as e:
        print(f"Ошибка: {e}")
        driver.save_screenshot("drag_error.png")
        assert False, f"Не удалось выполнить перетаскивание: {e}"
