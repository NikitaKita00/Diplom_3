from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    ACTIVE_PASSWORD_FIELD = (
        By.XPATH,
        "//input[@name='Пароль' and contains(@class, 'input__textfield-focused')]",
    )

    # Новые локаторы для полей ввода
    EMAIL_FIELD = (
        By.XPATH,
        "//*[@id='root']/div/main/div/form/fieldset[1]/div/div//input",
    )
    PASSWORD_FIELD = (
        By.XPATH,
        "//*[@id='root']/div/main/div/form/fieldset[2]/div/div//input",
    )
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/form/button")
