from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    
    # Теперь проверяем всё на странице логина
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()