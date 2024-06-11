from pages.AuthPage import AuthPage
import time

def test_first(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("salesakk@gmail.com", "111111Atlas1")

    time.sleep(4)
