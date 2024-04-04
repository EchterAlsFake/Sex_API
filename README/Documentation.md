# Sex API Documentation

> - Version 1.0
> - Author: Johannes Habel
> - Copyright (C) 2024
> - License: LGPLv3
> - Dependencies: requests, eaf_base_api

> [!IMPORTANT]
> This API is in violation of the Terms of Services of Sex.com. Usage is on your own risk!
> If you are the website owner of Sex.com, feel free to contact at my E-Mail, and I'll take this repository immediately 
> offline.  E-Mail: EchterAlsFake@proton.me

> The API is very well coded. I made it easy for modern IDEs to give you a good code suggestion, so you might be better off by reading the Source code :)

# Table of Contents
- [Installation](#installation)
- [The Client Object](#the-client)
- [The Pin Object](#the-pin-object)
- [The Tag Object](#the-tag-object)
- [The Comment Object](#the-comment-object)
- [The User Object](#the-user-object)
- [The Board Object](#the-board-object)

# Installation
- PyPi: `pip install sex_api`
- GitHub: `pip install git+https://github.com/EchterAlsFake/Sex_API`

> [!NOTE]
> Sex API should support Python 3.7+

# The Client
The Client is where all the functionality comes from.

```python
from sex_api.api import Client
client = Client()

# The client has the following functions:

pin = client.get_pin("<url>")     # Returns a Pin object
user = client.get_user("<url>")   # Returns a User object
board = client.get_board("<url>") # Returns a Board object
```

# The Pin object

```python
from sex_api.api import Client
client = Client()
pin = client.get_pin("<url>")

# After fetching the pin object, you can interact with its properties:
print(pin.name) # Returns the name (title) of the Pin
print(pin.publish_date) # Returns the publish date of the Pin
print(pin.embed_url) # Returns the embed / source URL of the Pin. Can be used to integrate into other websites
print(pin.tags) # Returns the Tag object
print(pin.get_comments) # Returns the Comment object

# Download a Pin:
pin.download("<output path directory>") # Returns True or False, whether download was successful
```

# The Tag object
```python
from sex_api.api import Client
client = Client()
pin = client.get_pin("<url>")

# You can get the tags from a Pin like this:
tags = pin.tags

# Now the tag object contains the names of the tags:
names = tags.names
for name in names:
    print(name)
```

# The Comment object
```python
from sex_api.api import Client
client = Client()
pin = client.get_pin("<url>")

# You can get the Comment object from a Pin like this:
comment = pin.get_comments

# The comment object contains the following data:
print(comment.comment_count) # The total count of comments
print(comment.ids) # The comment IDs (as a list)
print(comment.users) # The users who commented (as a list)
print(comment.messages) # The actual messages (as a list)
```

# The User object
```python
from sex_api.api import Client
client = Client()
user = client.get_user("<url>")

# You can access several attributes from users. Basically anything you could on the site.

print(user.description) # The User's description
print(user.username) # The username
print(user.amount_liked_pins) # The number of liked pins
print(user.count_boards) # The number of boards
print(user.count_following) # The count of following boards
print(user.count_pins) # The count of pins
print(user.count_repins) # The count of repins

# Now the interesting stuff:

pins = user.get_pins()
liked_pins = user.get_liked_pins()
boards = user.get_boards()
repins = user.get_repins()
following = user.get_following_boards()

# You can loop through all of these and get the Pin objects:

for pin in pins:
    print(pin.name) # Etc like described above in "The Pin object"
```

# The Board object
```python
from sex_api.api import Client
client = Client()
board = client.get_board("<url>")

# You can access several attributes from board objects:

print(board.get_pin_count) # Returns the total number of pins
print(board.get_follower_count) # Returns the total number of followers
print(board.total_pages_count) # Returns the total page count (may or may not work. It's a bit buggy sometimes)

# You can also get the Pins
pins = board.get_pins()

for pin in pins:
    print(pin.name) # ....
```


