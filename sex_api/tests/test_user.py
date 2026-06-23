import pytest
from ..api import Client


@pytest.fixture
def client():
    return Client()


@pytest.mark.asyncio
async def test_user_attributes(client):
    user = await client.get_user("https://www.sex.com/user/twitchxxx")
    assert isinstance(user.count_pins, str)
    assert isinstance(user.count_repins, str)
    assert isinstance(user.count_following, str)
    assert isinstance(user.count_boards, str)
    assert isinstance(user.amount_liked_pins, str)
    assert isinstance(user.username, str) and len(user.username) > 3
    assert isinstance(user.description, str) and len(user.description) > 3


@pytest.mark.asyncio
async def test_user_pins(client):
    user = await client.get_user("https://www.sex.com/user/twitchxxx")
    pins = user.get_pins()
    liked = user.get_liked_pins()
    repins = user.get_repins()

    idx = 0
    async for pin in pins:
        assert isinstance(pin.name, str) and len(pin.name) > 1

        if idx == 5:
            break
        idx += 1

    idx = 0
    async for pin in liked:
        assert isinstance(pin.name, str) and len(pin.name) > 1

        if idx == 5:
            break
        idx += 1

    idx = 0
    async for pin in repins:
        assert isinstance(pin.name, str) and len(pin.name) > 1

        if idx == 5:
            break
        idx += 1
