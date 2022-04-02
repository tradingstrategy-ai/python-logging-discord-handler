[![PyPI version](https://badge.fury.io/py/python-logging-discord-handler.svg)](https://badge.fury.io/py/python-logging-discord-handler)

[![Automated test suite](https://github.com/tradingstrategy-ai/python-logging-discord-handler/actions/workflows/tests.yml/badge.svg)](https://github.com/tradingstrategy-ai/python-logging-discord-handler/actions/workflows/tests.yml)

[![Documentation Status](https://readthedocs.org/projects/python-logging-discord-handler/badge/?version=latest)](https://python-logging-discord-handler.readthedocs.io/en/latest/?badge=latest)

# Python logging handler for Discord

Redirect your Python log output to Discord using [Python logging subsystem](https://docs.python.org/3/howto/logging.html) and [Discord Webhook library](https://github.com/lovvskillz/python-discord-webhook).

![Example screenshot](https://raw.githubusercontent.com/tradingstrategy-ai/python-logging-discord-handler/master/docs/source/_static/example_screenshot.png)

# Use cases

- Get notified on server-side errors
- Follow your batch job processes easily
- Good for businesses and communities that have their messaging set up in Discord 

# Features

- Minimum or no changes to a Python application needed
- Optional color coding of messages using [Discord embeds](https://discordjs.guide/popular-topics/embeds.html#embed-preview)
- Optional emoticons on messages using Unicode
- Discord rate limiting friendly for burst of logs
- Documentation
- Special handling for long log messages like tracebacks to deal with Discord's 2000 character max message length

# Usage

This example logs both to Discord and standard output. 

First you need to 

```python
import logging

from discord_logging.handler import DiscordHandler

# See instructions below how to get a Webhook URL
webhook_url = # ...
logger = logging.getLogger()

stream_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
discord_format = logging.Formatter("%(message)s")

discord_handler = DiscordHandler(
    "Hello World Bot", 
    webhook_url, 
    avatar_url="https://i0.wp.com/www.theterminatorfans.com/wp-content/uploads/2012/09/the-terminator3.jpg?resize=900%2C450&ssl=1")

#discord_handler = DiscordHandler("Happy Bot", webhook_url, emojis={})
discord_handler.setFormatter(discord_format)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_format)

# Add the handlers to the Logger
logger.addHandler(discord_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

logger.info("This is an info message")
logger.debug("A debug message - usually not that interesting")
logger.error("Very nasty error messgae!")
```

# How to get Discord webhook URL

1. Go to channel settings in Discord
2. Choose Integration
3. Create new webhook
4. Copy URL

# Discord limitations

- Max 2000 characters per message. See API documentation how to work around this limitation with different options. By default the bottom most lines of the log message, like a traceback, are shown.
- Discord embeds, those that give you a logging level color bar on the left, have very hard time to deal with long lines. Embeds are disabled for long lines by default.

## Log output formatting logic

The log message are converted to Discord embeds with the following logic

- Single line log messsages are converted to embed titles
- For multi line log messages, the first line is the embed title and the following lines are the embed description
- Long lines or long messages cannot be convert to embeds, instead they use [Discord Markdown code formattiong](https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-) to preserve the readability of the output

# Colours and emoticons

Logging messages can be decorated with colours and emoticons.

![Emoji screenshot](https://raw.githubusercontent.com/tradingstrategy-ai/python-logging-discord-handler/master/docs/source/_static/emoji_example.png)


Here are the defaults:

```python
# Colors as hexacimal, converted int
DEFAULT_COLOURS = {
    None: 2040357,
    logging.CRITICAL: 14362664,  # Red
    logging.ERROR: 14362664,  # Red
    logging.WARNING: 16497928,  # Yellow
    logging.INFO: 2196944,  # Blue
    logging.DEBUG: 8947848,  # Gray
}


DEFAULT_EMOJIS = {
    None: "",
    logging.CRITICAL: "🆘",
    logging.ERROR: "❌",
    logging.WARNING: "⚠️",
    logging.INFO: "",
    logging.DEBUG: "",
}
```

Emoticons are disabled by default as they often make the output a bit too colourful and harder to read.

# Testing and development

## Manual tests

Inspect how logging output looks in Discord.

- Checkout this Git repository
- Set up a dummy Discord channel
- Get its webhook URL

```shell
poetry install -E docs 
export DISCORD_TEST_WEBHOOK_URL=...
python discord_logging/handler.py
```

This will dump some messages to your Discord.

## Automated tests

Run:

```shell
pytest
```

# History

[Originally created for Trading Strategy](https://tradingstrategy.ai) to follow trading bot activity.

# License 

MIT
