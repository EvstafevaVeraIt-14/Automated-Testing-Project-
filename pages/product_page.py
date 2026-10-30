from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_btn.click()

    def should_be_add_to_basket_message(self):
        # Получаем название товара и сообщение о добавлении
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == success_message, f"Название товара не совпадает: {product_name} != {success_message}"

    def should_be_correct_basket_total(self):
        # Получаем цену товара и стоимость корзины
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, f"Цена не совпадает: {product_price} != {basket_total}"