import allure
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.password_recover_page import PasswordRecoverPage


class TestPasswordRecover:
    """Тесты восстановления пароля"""

    @allure.title("Поле пароля выделено при нажатии на глаз")
    @allure.description(
        "После нажатия на глаз поле пароля должно быть выделено (яркой рамкой)"
    )
    def test_email_active_on_eye_click(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_account()
        
        account_page = AccountPage(driver)
        account_page.go_to_password_recover()
        
        password_recover_page = PasswordRecoverPage(driver)
        password_recover_page.set_email("any_valid_mail@box.gu")
        password_recover_page.click_recover()
        
        password_recover_page.click_eye_button()
        assert password_recover_page.check_password_box_is_active()

    @allure.title("Переход на страницу восстановления пароля")
    @allure.description(
        "Проверка перехода с главной страницы на страницу восстановления (через ЛК)"
    )
    def test_goto_password_recover_start(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_account()
        
        account_page = AccountPage(driver)
        account_page.go_to_password_recover()
        
        password_recover_page = PasswordRecoverPage(driver)
        assert password_recover_page.check_start_page_is_present()

    @allure.title("Ввод почты и проверка кнопки Восстановить")
    @allure.description(
        "Проверка перехода к стр. сохранения нов.пароля при его восстановлении"
    )
    def test_goto_password_recover_save(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_account()
        
        account_page = AccountPage(driver)
        account_page.go_to_password_recover()
        
        password_recover_page = PasswordRecoverPage(driver)
        password_recover_page.set_email("any_valid_mail@box.gu")
        password_recover_page.click_recover()
        
        assert password_recover_page.check_save_page_is_present()
