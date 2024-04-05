from ..api import Client

client = Client()
board = client.get_board("https://www.sex.com/user/keymatt22/cum-on/")


def test_board_attributes():
    assert isinstance(board.get_pin_count, str) and len(board.get_pin_count) >= 1
    assert isinstance(board.total_pages_count, str) and len(board.total_pages_count) >= 1
    assert isinstance(board.get_follower_count, str) and len(board.get_follower_count) >= 1


def test_pins():
    pins = board.get_pins()

    for idx, pin in enumerate(pins):
        assert isinstance(pin.name, str) and len(pin.name) > 3

        if idx == 5:
            break
