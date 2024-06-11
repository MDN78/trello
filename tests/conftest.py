import pytest
import allure
from selenium import webdriver


@pytest.fixture
def browser():
    with allure.step("Open and prepare browser"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.maximize_window()

    yield browser

    with allure.step("Close browser"):
        browser.quit()
