from api.BoardApi import BoardApi
import allure
import pytest

def test_create_list(api_client: BoardApi, dummy_board_id: str, testdata: dict ):
    org_id = testdata.get("org_id")
    api_client.create_list("new list for test", dummy_board_id)
    board_lists = api_client.get_lists_by_board_id(dummy_board_id)
    assert len(board_lists) != 0
    api_client.delete_board_by_id(dummy_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    assert len(board_list_after) == 0