from ..api import Client, Mode, Relevance

client = Client()
searching = client.search("Mia Khalifa")


def test_searching():
    for idx, pin in enumerate(searching):
        assert isinstance(pin.name, str) and len(pin.name) > 3

        if idx == 5:
            break
