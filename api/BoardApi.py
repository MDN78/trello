import requests
import allure


class BoardApi:

    @allure.step("URL: {base_url}, auth token {token}")
    def __init__(self, base_url: str, key: str, token: str) -> None:
        self.base_url = base_url
        self.key = key
        self.token = token

    @allure.step("API. Get all boards for organization {org_id} ")
    def get_all_boards_by_org_id(self, org_id: str) -> list:
        path = "{trello}/organizations/{id}?boards=open&board_fields=all&fields=boards/".format(trello=self.base_url,
                                                                                                id=org_id)
        cookie = {
            'key': self.key,
            'token': self.token
        }
        print(path)
        resp = requests.get(path, params=cookie)
        return resp.json().get("boards")

    @allure.step("API. Create new board {name}")
    def create_board(self, name: str) -> dict:
        body = {
            "name": name,
            "key": self.key,
            "token": self.token
        }
        path = "{trello}/boards/".format(trello=self.base_url)
        resp = requests.post(path, params=body)
        return resp.json()

    @allure.step("API. Update card {card_id} - new name is {new_name}")
    def update_card(self, new_name: str, card_id: str) -> dict:
        headers = {
            "Accept": "application/json"
        }
        body = {
            "name": new_name,
            "key": self.key,
            "token": self.token
        }
        path = "{trello}/cards/{card_id}".format(trello=self.base_url, card_id=card_id)
        resp = requests.put(path, headers=headers, params=body,)
        return resp.json()

    @allure.step("API. Delete board with id {id}")
    def delete_board_by_id(self, id: str) -> dict:
        body = {
            "key": self.key,
            "token": self.token
        }
        path = "{trello}/boards/{board_id}".format(trello=self.base_url, board_id=id)
        resp = requests.delete(path, params=body)
        return resp.json()

    @allure.step("API. Create list {name} in board {board_id}")
    def create_list(self, name: str, board_id: str) -> dict:
        body = {
            "name": name,
            "idBoard": board_id,
            "key": self.key,
            "token": self.token,
        }
        path = "{trello}/boards/{board_id}/lists".format(trello=self.base_url, board_id=board_id)
        resp = requests.post(path, params=body)
        return resp.json()

    @allure.step("API. Create card {name} in list {list_id}")
    def create_card(self, name: str, list_id: str) -> str:
        headers = {
            "Accept": "application/json"
        }
        body = {
            "idList": list_id,
            "key": self.key,
            "token": self.token,
            "name": name
        }
        path = "{trello}/cards".format(trello=self.base_url)
        resp = requests.post(path, headers=headers, params=body)
        return resp.json()

    @allure.step("API. Get lists in board {board_id}")
    def get_lists_by_board_id(self, board_id: str) -> dict:
        path = "{trello}/boards/{board_id}/lists".format(trello=self.base_url, board_id=board_id)
        body = {
            "key": self.key,
            "token": self.token
        }
        resp = requests.get(path, params=body)
        return resp.json()
