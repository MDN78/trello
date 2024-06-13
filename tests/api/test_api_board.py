from api.BoardApi import BoardApi
import pytest
import allure


@pytest.mark.skip
def test_get_boards(api_client: BoardApi):
    board_list = api_client.get_all_boards_by_org_id('64158b830d737136d0131035')
    assert len(board_list) == 0
    print(board_list)

# @pytest.mark.skip
def test_create_board(api_client: BoardApi, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_org_id('64158b830d737136d0131035')
    resp = api_client.create_board('New board to be deleted')
    delete_board["board_id"] = resp.get("id")
    print(resp)
    board_list_after = api_client.get_all_boards_by_org_id('64158b830d737136d0131035')
    assert len(board_list_after) - len(board_list_before) == 1

@pytest.mark.skip
def test_delete_board(api_client: BoardApi, dummy_board_id: str):
    board_list_before = api_client.get_all_boards_by_org_id('64158b830d737136d0131035')
    resp = api_client.delete_board_by_id(dummy_board_id)
    print(resp)
    board_list_after = api_client.get_all_boards_by_org_id('64158b830d737136d0131035')
    assert len(board_list_before) - len(board_list_after) == 1
