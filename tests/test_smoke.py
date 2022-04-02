"""Check that the magic smoke stays inside the library.

Because most interaction happens with Discord any case, there is little automated testing we can do.
"""

import logging

from discord_logging.handler import DiscordHandler
import requests_mock


def test_rough():
    """Check that we pipe messages to Discord server."""

    logger = logging.getLogger()

    discord_handler = DiscordHandler(
        "Hello World Bot",
        "http://example.com/no-discord-webhook-url")

    logger.addHandler(discord_handler)

    # https://requests-mock.readthedocs.io/en/latest/mocker.html
    with requests_mock.Mocker() as discord_backend_mock:
        discord_backend_mock.get('http://example.com/', text='resp')
        logger.info("Hello Test")

