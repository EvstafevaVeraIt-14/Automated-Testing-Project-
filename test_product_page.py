from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    
    page.should_be_add_to_basket_message(product_name)
    page.should_be_correct_basket_total(product_price)