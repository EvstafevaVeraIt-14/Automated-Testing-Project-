from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code() # Решаем капчу и получаем код
    time.sleep(2) # Небольшая пауза, чтобы сообщения успели появиться
    
    # Проверки
    page.should_be_add_to_basket_message()
    page.should_be_correct_basket_total()