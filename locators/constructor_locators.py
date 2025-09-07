from selenium.webdriver.common.by import By


class ConstructorLocators:
    # Навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")
    ORDER_FEED_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[2]/a/p")

    # Ингредиенты
    INGREDIENT_ITEM = (
        By.XPATH,
        "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]",
    )
    DRAGGABLE_INGREDIENT = (
        By.XPATH,
        "//*[@id='root']/div/main/section[1]/div[2]/ul[2]/a[2]",
    )
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter__')]")

    # Модальное окно ингредиента
    MODAL_WINDOW = (By.XPATH, "/html/body/div/div/section/div[1]/div")
    MODAL_CLOSE_BUTTON = (By.XPATH, "/html/body/div/div/section/div[1]/button")

    # Альтернативные локаторы для модального окна
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_CLOSE_ALT = (By.XPATH, "//button[contains(@class, 'Modal_close__')]")

    # Конструктор бургера
    BURGER_CONSTRUCTOR = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket__')]",
    )
    ORDER_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")
    ORDER_TOTAL = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/div/p")

    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_order')]")

    # Навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")
    ORDER_FEED_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[2]/a/p")

    # Ингредиенты
    INGREDIENT_ITEM = (
        By.XPATH,
        "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]",
    )
    BUN_INGREDIENT = (
        By.XPATH,
        "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]",
    )  # Добавили этот локатор
    DRAGGABLE_INGREDIENT = (
        By.XPATH,
        "//*[@id='root']/div/main/section[1]/div[2]/ul[2]/a[2]",
    )
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter__')]")

    # Модальное окно ингредиента

    MODAL_CLOSE_BUTTON = (By.XPATH, "/html/body/div/div/section/div[1]/button")
    # Каунтеры ингредиентов
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter__')]")

    # Конструктор бургера
    BURGER_CONSTRUCTOR = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket__')]",
    )

    # Ингредиенты - самые простые локаторы
    ANY_INGREDIENT = (
        By.XPATH,
        "//a[contains(@class, 'BurgerIngredient_ingredient__')]",
    )
    BUN_INGREDIENT = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient__')])[1]",
    )
    SAUCE_INGREDIENT = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient__')])[2]",
    )
    FILLING_INGREDIENT = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient__')])[3]",
    )
