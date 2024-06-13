import requests
import allure


class BoardApi:
    # base_url = 'https://api.trello.com/1'

    def __init__(self, base_url: str, key: str, token: str) -> None:
        self.base_url = base_url
        self.key = key
        self.token = token

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

    def create_board(self, name: str) -> dict:
        body = {
            "name": name,
            "key": self.key,
            "token": self.token
        }
        path = "{trello}/boards/".format(trello=self.base_url)
        resp = requests.post(path, params=body)
        return resp.json()

    def delete_board_by_id(self, id: str) -> dict:
        body = {
            "key": self.key,
            "token": self.token
        }
        path = "{trello}/boards/{board_id}".format(trello=self.base_url, board_id=id)
        resp = requests.delete(path, params=body)
        return resp.json()
