import os
import requests
import html

from functools import cached_property
from base_api.base import Core, setup_api

setup_api(do_logging=True)

try:
    from modules.errors import *
    from modules.consts import *

except (ImportError, ModuleNotFoundError):
    from modules import *
    from modules.consts import *

class Comment:
    """
    Represents comments under a Pin
    """
    def __init__(self, html_content):
        self.html_content = html_content

    @cached_property
    def ids(self) -> list:
        """
        Cached Property
        :return: (list(str)) The comment IDs under the Pin
        """
        ids_ = regex_comment_id.findall(self.html_content)
        yield ids_

    @cached_property
    def users(self) -> list:
        """
        Cached Property
        :return: (list(str)) The usernames of commentators under the Pin
        """
        print(self.html_content)
        users_ = regex_comment_user.findall(self.html_content)
        yield users_

    @cached_property
    def messages(self) -> list:
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


class Search:
    def __init__(self):
        pass


class Tag:
    def __init__(self, html_content):
        self.html_content = html_content

    @cached_property
    def names(self):
        names = regex_tag_name.findall(self.html_content)
        yield names


class Pin:
    """
    Represents a Pin from Sex.com/pin/...
    """
    def __init__(self, url):
        self.session = Core().get_content(url=url, headers=headers, cookies=cookies)
        self.html_content = self.session.decode("utf-8")

    @cached_property
    def name(self):
        """
        :return: (str) The name of the Pin
        """
        name = regex_pin_name.search(self.html_content)
        return name.group(1)

    @cached_property
    def tags(self):
        """
        :return: (Tag) The tags of the Pin (as a Tag object)
        """
        return Tag(self.html_content)

    @cached_property
    def publish_date(self):
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

    def download(self, path) -> bool:
        """
        :param path: (str or PathLike object) The path, where the pin should be downloaded to
        :return: (bool) True if the download was successful, False otherwise.
        """
        print(self.html_content)
        match = regex_detect_video.search(self.html_content)

        if match:
            raise NotSupported("Sorry, but downloading this Pin is not supported. Remember, Clips (videos) are not "
                               "supported by this API!")

        download_url = []
        urls = regex_pin_download_url.findall(self.html_content)

        for url in urls:
            if str(url).startswith("https://cdn.sex.com/images/pinporn"):
                download_url.append(url)

        if len(download_url) >= 1:
            download_url = html.unescape(download_url[0])

        content = requests.get(url=download_url, headers=headers, cookies=cookies)
        download_content = content.content
        name = self.name

        if not str(path).endswith(os.sep):
            path += os.sep

        if ".gif" in download_url:
            file = open(f"{path}{name}.gif", "wb")

        elif ".jpg" in download_url:
            file = open(f"{path}{name}.jpg", "wb")

        else:
            return False

        try:
            file.write(download_content)
            return True

        except Exception as e:
            raise e


class Client:

    @classmethod
    def get_pin(cls, url):
        """
        :param url: (str) The URL of the Pin
        :return: (Pin) The Pin object which can be used to access the Pin and receive data from it and download it.
        """
        return Pin(url)
