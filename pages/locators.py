from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")    #ссылка на логин

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")    #форма логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")   #форма регистрации

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")    #кнопка добавления товара в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_BUY_ALERT_NAME = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    PRODUCT_BUY_ALERT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")