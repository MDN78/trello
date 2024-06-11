import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def test_auth(browser):
    email = "salesakk@gmail.com"
    password = "111111Atlas1"
    username = 'Dimitri'

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()
    with allure.step(f"Checking that {current_url} ends on /boards"):
        assert current_url.endswith("/boards")

    with allure.step("Checking user info"):
        assert info[0] == username
        assert info[1] == email
