from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
from .pages.login_page import LoginPageLocators



@pytest.mark.login_guest
class TestLoginMainPage():
    def test_guest_can_go_to_login_page(self, browser): #На страницу логина можно перейти
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                     #открываем страницу
        page.go_to_login_page()         #выполняем метод перейти на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):    #ссылка на логин есть
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser): #На странице корзины нет товаров
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()