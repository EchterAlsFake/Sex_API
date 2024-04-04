<h1 align="center">Sex.com API</h1> 

<div align="center">
    <a href="https://pepy.tech/project/sex_api"><img src="https://static.pepy.tech/badge/sex_api" alt="Downloads"></a>
    <a href="https://github.com/EchterAlsFake/sex_api/workflows/"><img src="https://github.com/EchterAlsFake/sex_api/workflows/CodeQL/badge.svg" alt="CodeQL Analysis"/></a>
    <a href="https://github.com/EchterAlsFake/sex_api/workflows/"><img src="https://github.com/EchterAlsFake/sex_api/actions/workflows/tests.yml/badge.svg" alt="API Tests"/></a>
</div>

# Description
Sex API is a Python API dedicated to Sex.com/pins. It allows you to download Pins, fetch information about Pins, Users and Boards.
You can also perform a search with filters.

> [!IMPORTANT]
> The Sex API is in violation of the Terms of Services of Sex.com. Usage is on your own risk!
> This API is related to sex.com/pins. This API does NOT support downloading videos from Sex.com nor video clips from sex.com/pins.
> The Videos are DRM locked, and the video clips need Javascript to be loaded.


# Quickstart
### Have a look at the [Documentation](https://github.com/EchterAlsFake/sex_api/blob/master/README/Documentation.md) for more details

- Install the library with `pip install sex_api`
- Or with: `pip install git+https://github.com/EchterAlsFake/sex_api` for the latest fixes / features

```python
from sex_api.api import Client

client = Client()

# Fetch a Pin
pin = client.get_pin("<URL>")
pin.download("<PATH (Directory)>")

# Print some attributes:
print(pin.name)
print(pin.publish_date) # See Docs for more

# Fetch a User:
user = client.get_user("URL")

# Get users Pins:
pins = user.get_pins()
pins_liked = user.get_liked_pins()

for pin in pins:
    pin.download("<path>")
    # ....... 
    
# The features are nearly endless. See Documentation for more :)
```

> [!NOTE]
> Sex API can also be run from the command line. Just execute: "xvideos_api -h" to get started.

# Changelog
See [Changelog](https://github.com/EchterAlsFake/sex_api/blob/master/README/Changelog.md) for more details.

# Contribution
Do you see any issues or having some feature requests? Simply open an Issue or talk
in the discussions.

Pull requests are also welcome.

# License
Licensed under the LGPLv3 License

Copyright (C) 2023–2024 Johannes Habel