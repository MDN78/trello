from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
import time

def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("salesakk@gmail.com", "111111Atlas1")

    assert auth_page.get_current_url().endswith("/boards")

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()
    assert info[0] == 'Dimitri'
    assert info[1] == "salesakk@gmail.com"


    time.sleep(2)
