"""Check that the magic smoke stays inside the library.

Because most interaction happens with Discord any case, there is little automated testing we can do.
"""

import logging
from typing import Optional
from urllib.request import Request

from discord_logging.examples import log_examples
from discord_logging.handler import DiscordHandler
import requests_mock


def test_rough():
    """Check that we pipe messages to Discord server."""

    request_payload: Optional[dict] = None

    def callback(request: Request, context):
        nonlocal request_payload
        print(type(request), context)
        request_payload = request.json()

    # https://requests-mock.readthedocs.io/en/latest/mocker.html
    with requests_mock.Mocker() as discord_backend_mock:
        discord_backend_mock.post('http://example.com/no-discord-webhook-url', text=callback)
        log_examples("http://example.com/no-discord-webhook-url")

    # We successfully made a HTTP POST to mocked Discord server
    assert request_payload["username"] == "My server log example"
