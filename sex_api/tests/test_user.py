from ..api import Client

client = Client()
user = client.get_user("https://www.sex.com/user/twitchxxx")


def test_user_attributes():
    assert isinstance(user.count_pins, str)
    assert isinstance(user.count_repins, str)
    assert isinstance(user.count_following, str)
    assert isinstance(user.count_boards, str)
    assert isinstance(user.amount_liked_pins, str)
    assert isinstance(user.username, str) and len(user.username) > 3
    assert isinstance(user.description, str) and len(user.description) > 3


def test_user_pins():
    pins = user.get_pins()
    liked = user.get_liked_pins()
    repins = user.get_repins()

    for idx, pin in enumerate(pins):
        assert isinstance(pin.name, str) and len(pin.name) > 1

        if idx == 5:
            break

    for idx, pin in enumerate(liked):
        assert isinstance(pin.name, str) and len(pin.name) > 1

        if idx == 5:
            break

    for idx, pin in enumerate(repins):
        assert isinstance(pin.name, str) and len(pin.name) > 1

        if idx == 5:
            break
