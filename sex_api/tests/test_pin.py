from ..api import Client, Tag, Comment

client = Client()
pin = client.get_pin("https://www.sex.com/pin/66118934-model-anna-l/")


def test_pin():
    assert isinstance(pin.embed_url, str) and len(pin.embed_url) > 3
    assert isinstance(pin.name, str) and len(pin.name) > 3
    assert isinstance(pin.tags, Tag)
    assert isinstance(pin.get_comments, Comment)
    assert isinstance(pin.publish_date, str) and len(pin.publish_date) > 3
