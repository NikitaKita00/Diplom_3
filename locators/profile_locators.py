from selenium.webdriver.common.by import By


class ProfileLocators:
    # Навигация в личном кабинете
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button")
    LOGOUT_BUTTON_ALT = (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")

    # Поля профиля
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")

    # Кнопка личного кабинета в хедере
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")

    # Модальное окно (если есть)
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")

    # Элементы для проверки страницы профиля
    PROFILE_SECTION = (By.XPATH, "//div[contains(@class, 'Account_account__')]")
