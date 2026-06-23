import pytest
from ..api import Client, Mode, Relevance


@pytest.fixture
def client():
    return Client()


@pytest.mark.asyncio
async def test_searching(client):
    searching = client.search("Mia Khalifa")

    idx = 0
    async for pin in searching:
        assert isinstance(pin.name, str) and len(pin.name) > 3

        if idx == 5:
            break
        idx += 1
