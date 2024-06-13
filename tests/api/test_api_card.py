from api.BoardApi import BoardApi
import allure
import pytest

@pytest.mark.skip
def test_create_list(api_client: BoardApi, dummy_board_id: str, testdata: dict ):
    org_id = testdata.get("org_id")
    api_client.create_list("new list for test", dummy_board_id)
    board_lists = api_client.get_lists_by_board_id(dummy_board_id)
    assert len(board_lists) != 0
    api_client.delete_board_by_id(dummy_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    assert len(board_list_after) == 0

@pytest.mark.skip
def test_edit_cart(api_client: BoardApi, dummy_card_id: str, testdata: dict):
    new_card = api_client.update_card("Foxtrot", dummy_card_id[1])
    assert new_card["name"] == "Foxtrot"
    api_client.delete_board_by_id(dummy_card_id[0])
    org_id = testdata.get("org_id")
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    assert len(board_list_after) == 0