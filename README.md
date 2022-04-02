# Python logging handler for Discord

Redirect your Python log output to Discord.

# Use cases

- Get notified on server-side errors
- Follow your batch job processes easily
- Good for businesses and communities that have their messaging set up in Discord 

# Features

- Minimum or no changes to a Python application needed
- Optional color coding of messages using embeds
- Optional emoticons on messages using Unicode
- Rate limiting friendly
- Documentation
- Special handling for long log messages like tracebacks to deal with Discord's 2000 character max message length

# Usage

```python

```

# How to get Discord webhook URL

1. Go to channel settings in Discord
2. Choose Integration
3. Create new webhook
4. Copy URL

# Testing and development

Only manual testing supported due to Discord integration.

- Checkout this Git repository
- Set up a dummy Discord channel
- Get its webhook URL

```shell
poetry install -E docs 
export DISCORD_TEST_WEBHOOK_URL=...
python discord_logging/handler.py
```

This will dump some messages to your Discord.

# History

[Originally created for Trading Strategy](https://tradingstrategy.ai) to follow trading bot activity.

# License 

MIT
