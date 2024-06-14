from api.BoardApi import BoardApi
from utils.validator_json import validator_json_scheme
import pytest
import allure

@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Get lists of all boards")
@pytest.mark.skip
def test_get_boards(api_client: BoardApi, testdata: dict):
    org_id = testdata.get("org_id")
    board_list = api_client.get_all_boards_by_org_id(org_id)
    assert len(board_list) == 0
    print(board_list)
    # with allure.step('Schema is validate'):
    #     validator_json_scheme(resp, 'list.json')

@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Create new board")
@pytest.mark.skip
def test_create_board(api_client: BoardApi, delete_board: dict, testdata: dict):
    org_id = testdata.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    resp = api_client.create_board('New board to be deleted')
    delete_board["board_id"] = resp.get("id")
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    assert len(board_list_after) - len(board_list_before) == 1
    with allure.step('Schema is validate'):
        validator_json_scheme(resp, 'create_board_scheme.json')

@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Delete board")
@pytest.mark.skip
def test_delete_board(api_client: BoardApi, dummy_board_id: str, testdata: dict):
    org_id = testdata.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    resp = api_client.delete_board_by_id(dummy_board_id)
    print(resp)
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    assert len(board_list_before) - len(board_list_after) == 1
