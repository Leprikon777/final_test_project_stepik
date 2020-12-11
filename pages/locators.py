from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini .btn-default")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")    #форма логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")   #форма регистрации

    EMAIL_REGISTER_INPUT = (By.CSS_SELECTOR, "#id_registration-email") #поле почты
    PASSWORD1_REGISTER_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_REGISTER_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")    #кнопка добавления товара в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_BUY_ALERT_NAME = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    PRODUCT_BUY_ALERT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")     #Надо будет подобрать корректный локатор
