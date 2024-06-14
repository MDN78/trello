import allure
import pytest
from api.BoardApi import BoardApi
from utils.validator_json import validator_json_scheme


@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Create list")
# @pytest.mark.skip
def test_create_list(api_client: BoardApi, dummy_board_id: str, testdata: dict):
    org_id = testdata.get("org_id")
    resp = api_client.create_list("new list for test", dummy_board_id)
    board_lists = api_client.get_lists_by_board_id(dummy_board_id)
    assert len(board_lists) != 0
    api_client.delete_board_by_id(dummy_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    assert len(board_list_after[0]) == 0
    with allure.step('Schema is validate'):
        validator_json_scheme(resp, 'list.json')


@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Edit card")
# @pytest.mark.skip
def test_edit_cart(api_client: BoardApi, dummy_card_id: str, testdata: dict):
    status = api_client.update_card("Foxtrot", dummy_card_id[1])
    api_client.delete_board_by_id(dummy_card_id[0])
    org_id = testdata.get("org_id")
    board_list_after = api_client.get_all_boards_by_org_id(org_id)

    with allure.step('Status code=200'):
        assert status[1] == 200
    with allure.step('Check request - response'):
        assert status[0]["name"] == "Foxtrot"
        assert len(board_list_after[0]) == 0
    with allure.step('Schema is validate'):
        validator_json_scheme(status[0], 'list.json')


@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Move card to another list")
# @pytest.mark.skip
def test_move_cart(api_client: BoardApi, dummy_card_id: list):
    board_list_before = api_client.get_lists_by_board_id(dummy_card_id[0])
    additional_list = api_client.create_list("List for moving card", dummy_card_id[0]).get("id")
    status = api_client.move_card(additional_list, dummy_card_id[1])
    board_lists_after = api_client.get_lists_by_board_id(dummy_card_id[0])
    api_client.delete_board_by_id(dummy_card_id[0])

    with allure.step('Status code=200'):
        assert status[1] == 200
    with allure.step('Check request - response'):
        assert len(board_lists_after) > len(board_list_before)
        assert status[0]["name"] != []
    with allure.step('Schema is validate'):
        validator_json_scheme(status[0], 'list.json')


@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Delete card")
# @pytest.mark.skip
def test_delete_card(api_client: BoardApi, dummy_card_id: list, testdata: dict):
    card_info_before = api_client.get_cards_in_list(dummy_card_id[2])
    status = api_client.delete_card(dummy_card_id[1])
    card_info_after = api_client.get_cards_in_list(dummy_card_id[2])
    api_client.delete_board_by_id(dummy_card_id[0])

    with allure.step('Status code=200'):
        assert status == 200
    with allure.step('Check card availability'):
        assert card_info_before != []
    with allure.step('Check that card was deleted'):
        assert card_info_after == []


