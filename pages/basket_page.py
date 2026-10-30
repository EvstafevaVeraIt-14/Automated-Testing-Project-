from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "В корзине есть товары, хотя их быть не должно"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Нет сообщения о том, что корзина пуста"
        
        # Проверяем сам текст
        message_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "empty" in message_text.lower(), f"Текст сообщения неверный: {message_text}"