import pytest
import allure
import requests
from selenium import webdriver
from api.BoardApi import BoardApi
from testdata.DataProvider import DataProvider
from configuration.ConfigProvider import ConfigProvider
import json

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
    resp = api.create_board('Board to be deleted')
    resp1 = resp[0].get("id")
    return resp1


@pytest.fixture
def dummy_card_id() -> list:
    url = ConfigProvider().get("api", "base_url")
    key = DataProvider().get_key()
    token = DataProvider().get_token()
    api = BoardApi(url, key, token)
    board = api.create_board("Board to be deleted")
    board1 = board[0].get("id")
    resp = api.create_list("List for test 2", board1).get("id")
    card = api.create_card("New test card",resp)
    return [board1, card["id"], resp]

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
        # cookie = {
        #     "key": data.get_key(),
        #     "token": data.get_token(),
        #     "value": "Finish Final Presentation"
        # }
        # cookie = {
        #     'name': 'key',
        #     'value': data.get_key()
        # }
        # # driver.
        # driver.add_cookie(cookie)
        # path = "https://api.trello.com/1/64158b830d737136d0131035"
        # cookie = {
        #     'name': 'Cookie',
        #     'value': 'dsc=5d7738312650e9b438d71866c2e0e278f77f4ef80c9019be226fa8ff9002dfb0',
        # }


        # url = "https://api.trello.com/1/members/me"
        #
        # payload = {}
        # headers = {
        #     'Authorization': f'OAuth oauth_consumer_key="{data.get_key()}", oauth_token="{data.get_token()}"',
        #     'Cookie': 'dsc=5d7738312650e9b438d71866c2e0e278f77f4ef80c9019be226fa8ff9002dfb0'
        # }
        #
        # response = requests.request("PUT", url, headers=headers, data=payload)
        # cookie = response.cookies
        # print(response.text)
        # 'https://id.atlassian.com/login?application=trello'
        url1 = 'https://id.atlassian.com/login?application=trello'
        login = "salesakk@gmail.com"
        password = '111111Atlas1'

        payload = {"action": "login", "email": login, "password": password}
        payload_json = json.dumps(payload)
        headers = {
            'content-type': 'application/json; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest'
        }

        result = requests.post(url1, headers=headers, data=payload_json)

        cookies = result.cookies.get_dict()

        # result = requests.post(url=url1, data={'email': login, 'password': password})
        # print(result)
        # cookie = result.cookies
        print(cookies)
        print(cookies['atlassian.account.ffs.id'])
        cookie = {
            "name": "atlassian.account.ffs.id",
            "value": cookies['atlassian.account.ffs.id']
        }
        driver.add_cookie(cookie)
        # driver.get(url)
        # driver.add_cookie(cookies)
        driver.refresh()
        driver.refresh()
        yield driver

    with allure.step("Close browser"):
        driver.quit()


