import pytest
import allure
from api.BoardApi import BoardApi
from utils.validator_json import validator_json_scheme



@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Get lists of all boards")
@pytest.mark.skip
def test_get_boards(api_client: BoardApi, testdata: dict):
    org_id = testdata.get("org_id")
    board_list = api_client.get_all_boards_by_org_id(org_id)
    status_code = board_list[1]

    with allure.step('Status code=200'):
        assert status_code == 200
    with allure.step('Check request - response'):
        assert len(board_list[0]) == 0
    with allure.step('Schema is validate'):
        validator_json_scheme(board_list[2], 'create_board_scheme.json')


@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Create new board")
@pytest.mark.skip
def test_create_board(api_client: BoardApi, delete_board: dict, testdata: dict):
    org_id = testdata.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    resp = api_client.create_board('New board to be deleted')
    status_code = resp[1]
    delete_board["board_id"] = resp[0].get("id")
    board_list_after = api_client.get_all_boards_by_org_id(org_id)

    with allure.step('Status code=200'):
        assert status_code == 200
    with allure.step('Check request - response'):
        assert len(board_list_after[0]) - len(board_list_before[0]) == 1
    with allure.step('Schema is validate'):
        validator_json_scheme(resp[0], 'create_board_scheme.json')


@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Delete board")
@pytest.mark.skip
def test_delete_board(api_client: BoardApi, dummy_board_id: str, testdata: dict):
    org_id = testdata.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    status = api_client.delete_board_by_id(dummy_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(org_id)

    with allure.step('Status code=200'):
        assert status == 200
    with allure.step('Check request - response'):
        assert len(board_list_before[0]) - len(board_list_after[0]) == 1
