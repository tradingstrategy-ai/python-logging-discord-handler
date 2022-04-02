# Python logging handler for Discord

Redirect your Python log output to Discord using [Python logging subsystem](https://docs.python.org/3/howto/logging.html) and [Discord Webhook library](https://github.com/lovvskillz/python-discord-webhook).

# Use cases

- Get notified on server-side errors
- Follow your batch job processes easily
- Good for businesses and communities that have their messaging set up in Discord 

# Features

- Minimum or no changes to a Python application needed
- Optional color coding of messages using embeds
- Optional emoticons on messages using Unicode
- Discord rate limiting friendly for burst of logs
- Documentation
- Special handling for long log messages like tracebacks to deal with Discord's 2000 character max message length

# Usage

This example logs both to Discord and standard output. 

First you need to 

```python
import logging

# See instructions below how to get a Webhook URL
webhook_url = os.environ["DISCORD_TEST_WEBHOOK_URL"]
logger = logging.getLogger()

stream_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
discord_format = logging.Formatter("%(message)s")

discord_handler = DiscordHandler(
    "Hello World Bot", 
    webhook_url, 
    emojis={}, 
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
