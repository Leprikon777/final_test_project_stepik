from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        busket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        busket_button.click()

    def product_message_is_correct(self):
        self.name_is_correct()
        self.price_is_correct()




    def name_is_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        alert_name = self.browser.find_element(*ProductPageLocators.PRODUCT_BUY_ALERT_NAME)
        assert product_name.text == alert_name.text, "Название купленного товара не соответствует тому, что на странице"

    def price_is_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        alert_price = self.browser.find_element(*ProductPageLocators.PRODUCT_BUY_ALERT_PRICE)
        assert product_price.text == alert_price.text, "Цена в сообщении не соответствует той, что на странице"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_hide_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not hide after some seconds"