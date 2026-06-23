import pytest
from ..api import Client


@pytest.fixture
def client():
    return Client()


@pytest.mark.asyncio
async def test_board_attributes(client):
    board = await client.get_board("https://www.sex.com/user/keymatt22/my-personal-favs/")
    assert isinstance(board.get_pin_count, str) and len(board.get_pin_count) >= 1
    assert isinstance(board.total_pages_count, str) and len(board.total_pages_count) >= 1
    assert isinstance(board.get_follower_count, str) and len(board.get_follower_count) >= 1


@pytest.mark.asyncio
async def test_pins(client):
    board = await client.get_board("https://www.sex.com/user/keymatt22/my-personal-favs/")
    pins = board.get_pins()

    idx = 0
    async for pin in pins:
        assert isinstance(pin.name, str) and len(pin.name) > 3

        if idx == 5:
            break
        idx += 1
