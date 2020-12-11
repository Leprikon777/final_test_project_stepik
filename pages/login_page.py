from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", f"Неправильный адрес страницы: {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Нет формы логина"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Нет формы регистрации"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_INPUT)
        password1_input = self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTER_INPUT)
        password2_input = self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTER_INPUT)
        #Передаем в элементы логин/пароль
        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        #Нажимаем на кнопку "Зарегистрироваться"
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
