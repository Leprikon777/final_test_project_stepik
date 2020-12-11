from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_correct_url()
        self.should_be_message_empty_basket()
        self.should_be_not_product()

    def should_be_correct_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/basket/", "Неверный адрес страницы корзины с товарами"
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE)
    def should_be_not_product(self):
        assert not self.is_element_present(*BasePageLocators.PRODUCT_IN_BASKET)