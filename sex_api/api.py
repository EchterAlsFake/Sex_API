import os
import html
import argparse

from curl_cffi import AsyncSession
from base_api.base import BaseCore
from functools import cached_property
from typing import Generator, AsyncGenerator

try:
    from modules.errors import *
    from modules.consts import *
    from modules.searching_filters import *

except (ImportError, ModuleNotFoundError):
    from .modules import *
    from .modules.consts import *
    from .modules.searching_filters import *


class Comment:
    """
    Represents comments under a Pin
    """
    def __init__(self, html_content):
        self.html_content = html_content

    @cached_property
    def ids(self) -> Generator[int, None, None]:
        """
        Cached Property
        :return: (list(str)) The comment IDs under the Pin
        """
        ids_ = regex_comment_id.findall(self.html_content)
        yield ids_

    @cached_property
    def users(self) -> Generator[str, None, None]:
        """
        Cached Property
        :return: (list(str)) The usernames of commentators under the Pin
        """
        users_ = regex_comment_user.findall(self.html_content)
        yield users_

    @cached_property
    def messages(self) -> Generator[str, None, None]:
        """
        Cached Property
        :return: (list(str)) The content of messages (comments) under the Pin
        """
        messages_ = regex_comment_messages.findall(self.html_content)
        yield messages_

    @cached_property
    def comment_count(self) -> int:
        """
        Cached Property
        :return: (int) The total comment count
        """
        comment_count_ = regex_comment_count.search(self.html_content)
        return int(comment_count_.group(1))


class Tag:
    def __init__(self, html_content):
        self.html_content = html_content

    @cached_property
    def names(self) -> Generator[str, None, None]:
        names = regex_tag_name.findall(self.html_content)
        yield names


class Pin:
    """
    Represents a Pin from Sex.com/pin/...
    """
    def __init__(self, url: str, core: BaseCore, html_content: str | None = None):
        self.core = core
        self.url = url
        self.html_content = html_content

    async def init(self):
        if not self.html_content:
            self.html_content = await self.core.fetch(url=self.url)

        return self

    @cached_property
    def name(self) -> str:
        """
        :return: (str) The name of the Pin
        """
        name = regex_pin_name.search(self.html_content)
        return name.group(1)

    @cached_property
    def tags(self) -> Tag:
        """
        :return: (Tag) The tags of the Pin (as a Tag object)
        """
        return Tag(self.html_content)

    @cached_property
    def publish_date(self) -> str:
        """
        :return: (str) The publication date of the Pin
        """
        date = regex_pin_publish_date.search(self.html_content)
        return date.group(1)

    @cached_property
    def get_comments(self) -> Comment:
        """
        :return: (Comment) The comment object for the Pin, which can be used to access the messages, ids, usernames etc.
        """
        return Comment(self.html_content)

    @cached_property
    def embed_url(self) -> str:
        """Returns the embed / source URL of the Pin. Can be used for integrating a Pin into your own website"""
        download_url = []
        urls = regex_pin_download_url.findall(self.html_content)

        for url in urls:
            if "pinporn" in url:
                download_url.append(url)

        return html.unescape(download_url[0])

    async def download(self, path) -> bool:
        """
        :param path: (str or PathLike object) The path, where the pin should be downloaded to
        :return: (bool) True if the download was successful, False otherwise.
        """
        match = regex_detect_video.search(self.html_content)

        if match:
            raise NotSupported("Sorry, but downloading this Pin is not supported. Remember, Clips (videos) are not "
                               "supported by this API!")

        download_content = await self.core.fetch(url=self.embed_url, get_bytes=True)
        name = self.name

        if not str(path).endswith(os.sep):
            path += os.sep

        if ".gif" in self.embed_url:
            file = open(f"{path}{name}.gif", "wb")

        elif ".jpg" in self.embed_url:
            file = open(f"{path}{name}.jpg", "wb")

        elif ".webp" in self.embed_url:
            file = open(f"{path}{name}.webp", "wb")

        else:
            return False

        try:
            file.write(download_content)
            file.close()
            return True

        except Exception as e:
            raise e


class Board:
    def __init__(self, url: str, core: BaseCore, html_content: str | None = None):
        self.core = core
        self.url = url
        self.html_content = html_content

    async def init(self):
        if not self.html_content:
            self.html_content = await self.core.fetch(self.url)

        return self

    @cached_property
    def total_pages_count(self) -> str:
        return regex_get_total_pages.search(self.html_content).group(1)

    @cached_property
    def get_follower_count(self) -> str:
        return regex_follower_count.search(self.html_content).group(1)

    @cached_property
    def get_pin_count(self) -> str:
        return regex_pin_count.search(self.html_content).group(1)

    async def get_pins(self) -> AsyncGenerator[Pin, None]:
        for page in range(1, 99):  # There is a really weird error when using @total_pages_count........ idk man...
            try:
                content = await self.core.fetch(f"{self.url}?page={page}")
                urls = regex_extract_pins.findall(content)

            except (AttributeError, TypeError): # Type error because it returns "Response" object from base API if 404
                break

            for url in urls:
                pin = Pin(f"https://sex.com{url}", core=self.core)
                yield await pin.init()


class User:
    def __init__(self, url: str, core: BaseCore, html_content: str | None = None):
        self.core = core
        self.url = url
        self.html_content = html_content

    async def init(self):
        if not self.html_content:
            self.html_content = await self.core.fetch(self.url)

        return self

    @cached_property
    def username(self) -> str:
        """Returns the username of the User"""
        return regex_extract_name.search(self.html_content).group(1)

    @cached_property
    def description(self) -> str:
        """Returns the description of the User"""
        return regex_description.search(self.html_content).group(1)

    @cached_property
    def count_boards(self) -> str:
        """Returns the total count of boards by the User"""
        return regex_amount_boards.search(self.html_content).group(1)

    @cached_property
    def count_following(self) -> str:
        """Returns the total count of users following the User"""
        return regex_amount_following.search(self.html_content).group(1)

    @cached_property
    def count_pins(self) -> str:
        """Returns the total count of Pins the User has"""
        return regex_amount_pins.search(self.html_content).group(1)

    @cached_property
    def count_repins(self) -> str:
        """Returns the total count ot repins the User has"""
        return regex_amount_repins.search(self.html_content).group(1)

    @cached_property
    def amount_liked_pins(self) -> str:
        """Returns the total count of liked Pins the User has"""
        return regex_amount_likes.search(self.html_content).group(1)

    async def get_boards(self) -> AsyncGenerator[Board, None]:
        """Returns the Boards from the User (as a Board object)"""
        urls = regex_get_boards.findall(self.html_content)
        for url in urls:
            board = Board(f"https://sex.com{url}", core=self.core)
            yield await board.init()

    async def get_following_boards(self) -> AsyncGenerator[Board, None]:
        """Returns the Boards the user if following too (as a Board object)"""
        content = await self.core.fetch(f"{self.url}/following/")
        urls = regex_get_boards.findall(content)
        for url in urls:
            board = Board(f"https://sex.com{url}", core=self.core)
            yield await board.init()

    async def get_pins(self) -> AsyncGenerator[Pin, None]:
        """Returns the Pins of the User (as a Pin object)"""
        for page in range(1, 99):
            try:
                content = await self.core.fetch(f"{self.url}/pins/?page={page}")
                urls = regex_extract_pins.findall(content)

            except (AttributeError, TypeError):
                break

            for url in urls:
                pin = Pin(f"https://sex.com{url}", core=self.core)
                yield await pin.init()

    async def get_repins(self) -> AsyncGenerator[Pin, None]:
        """Returns the Repins of the User (as a Pin object)"""
        for page in range(1, 99):
            try:
                content = await self.core.fetch(f"{self.url}/repins/?page={page}")
                urls = regex_extract_pins.findall(content)

            except (AttributeError, TypeError):
                break

            for url in urls:
                pin = Pin(f"https://sex.com{url}", core=self.core)
                yield await pin.init()

    async def get_liked_pins(self) -> AsyncGenerator[Pin, None]:
        """Returns the liked Pins of the User (as a Pin object)"""
        for page in range(1, 99):
            try:
                content = await self.core.fetch(f"{self.url}/likes/?page={page}")
                urls = regex_extract_pins.findall(content)

            except (AttributeError, TypeError):
                break

            for url in urls:
                pin = Pin(f"https://sex.com{url}", core=self.core)
                yield await pin.init()


class Client:
    def __init__(self, core: BaseCore = BaseCore()):
        self.core = core
        self.core.initialize_session()
        assert isinstance(self.core.session, AsyncSession)
        self.core.session.headers.update(headers)

    async def get_pin(self, url) -> Pin:
        """
        :param url: (str) The URL of the Pin
        :return: (Pin) The Pin object which can be used to access the Pin and receive data from it and download it.
        """
        pin = Pin(url, core=self.core)
        return await pin.init()

    async def search(self, query, sort_relevance: Relevance | str = Relevance.popular, mode: Mode | str = Mode.pics,
               pages: int = 5) -> AsyncGenerator[Pin | User | Board, None]:
        """
        :param query: (str) The search query
        :param sort_relevance: (Relevance) The Relevance object (see searching_filters.py)
        :param mode: (Mode) The Mode object (see searching_filters.py)
        :param pages: (int) The page count (one page contains ~50-60 Pins)
        """
        query = query.replace(" ", "+")

        for page in range(1, pages):
            content = await self.core.fetch(url=f"https://sex.com/search/{mode}?query={query}{sort_relevance}&page={page}",
                                 cookies=cookies)

            if mode == "pics" or mode == "gifs" or mode == "clips":
                pins = regex_extract_pins.findall(content)

                for pin in pins:
                    pin = Pin(f"https://sex.com{pin}", core=self.core)
                    yield await pin.init()

            elif mode == "users":
                users = regex_get_users.findall(content)
                for user in users:
                    user = User(f"https://sex.com{user}", core=self.core)
                    yield await user.init()

            elif mode == "boards":
                boards = regex_get_boards.findall(content)
                for board in boards:
                    board = Board(f"https://sex.com{board}", core=self.core)
                    yield await board.init()

    async def get_user(self, url) -> User:
        """
        :param url: (str) The URL of the User
        :return User: Returns the User object
        """
        user = User(url, core=self.core)
        return await user.init()

    async def get_board(self, url) -> Board:
        """
        :param url: (str) The URL of the Board
        :return Board: Returns the Board object
        """
        board = Board(url, core=self.core)
        return await board.init()


async def main():
    parser = argparse.ArgumentParser(description="Sex.com API Command Line Interface")
    parser.add_argument("--download", type=str, help="The Pin URL")
    parser.add_argument("--output", type=str, help="The Output Path (directory)")
    parser.add_argument("--board", type=str, help="URL to download a whole board")
    args = parser.parse_args()
    client = Client()

    if args.download:

        pin = await client.get_pin(args.download)
        await pin.download(path=args.output)

    if args.board:
        board = await client.get_board(args.board)
        pins = board.get_pins()

        async for pin in pins:
            await pin.download(path=args.output)
