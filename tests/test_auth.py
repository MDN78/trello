from pages.AuthPage import AuthPage
import time

def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("salesakk@gmail.com", "111111Atlas1")

    assert auth_page.get_current_url().endswith("/boards")

    time.sleep(2)
