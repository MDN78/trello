import pytest
import allure
from selenium import webdriver
from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider


@pytest.fixture
def driver():
    with allure.step("Open and prepare browser"):
        timeout = ConfigProvider().getint("ui", "timeout")
        driver_name = ConfigProvider().get("ui", "browser_name")
        driver = None

        if driver_name == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        driver.implicitly_wait(timeout)
        driver.maximize_window()
        yield driver

    with allure.step("Close browser"):
        driver.quit()


@pytest.fixture
def api_client() -> BoardApi:
    url = ConfigProvider().get("api", "base_url")
    key = DataProvider().get_key()
    token = DataProvider().get_token()
    return BoardApi(base_url=url, key=key, token=token)


@pytest.fixture
def api_client_no_auth() -> BoardApi:
    url = ConfigProvider().get("api", "base_url")
    key = DataProvider().get_key()
    token = ''
    return BoardApi(base_url=url, key=key, token=token)


@pytest.fixture
def dummy_board_id() -> str:
    url = ConfigProvider().get("api", "base_url")
    key = DataProvider().get_key()
    token = DataProvider().get_token()
    api = BoardApi(base_url=url, key=key, token=token)
    resp = api.create_board('Board to be deleted').get("id")
    return resp


@pytest.fixture
def delete_board() -> str:
    dictionary = {"board_id": ""}
    yield dictionary
    url = ConfigProvider().get("api", "base_url")
    key = DataProvider().get_key()
    token = DataProvider().get_token()
    api = BoardApi(base_url=url, key=key, token=token)
    api.delete_board_by_id(dictionary.get("board_id"))


@pytest.fixture
def testdata() -> dict:
    return DataProvider()


@pytest.fixture
def driver_auth():
    with allure.step("Open and prepare browser"):
        timeout = ConfigProvider().getint("ui", "timeout")

        driver_name = ConfigProvider().get("ui", "browser_name")
        driver = None

        if driver_name == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        driver.implicitly_wait(timeout)
        driver.maximize_window()
        url = ConfigProvider().get("ui", "base_url")
        driver.get(url)
        data = DataProvider()
        cookie = {
            "name": "token",
            "value": data.get_token()
        }
        driver.add_cookie(cookie)
        driver.refresh()
        driver.refresh()
        yield driver

    with allure.step("Close browser"):
        driver.quit()