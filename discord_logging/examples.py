"""Log output examples"""
import logging
import textwrap

from discord_logging.handler import DiscordHandler


def log_examples(webhook_url: str):
    """Log example output messages to stdout and Discord."""

    logger = logging.getLogger()

    # Silence requests and discord_webhook internals as otherwise this example will be too noisy
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("discord_webhook").setLevel(logging.FATAL)  # discord_webhook.webhook - ERROR - Webhook rate limited: sleeping for 0.235 seconds...

    stream_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    discord_format = logging.Formatter("%(message)s")

    discord_handler = DiscordHandler("My server log example", webhook_url, emojis={}, avatar_url="https://i0.wp.com/www.theterminatorfans.com/wp-content/uploads/2012/09/the-terminator3.jpg?resize=900%2C450&ssl=1")
    #discord_handler = DiscordHandler("Happy Bot", webhook_url, emojis={})
    discord_handler.setFormatter(discord_format)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(stream_format)

    # Add the handlers to the Logger
    logger.addHandler(discord_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)

    logger.info("Long line of text Long line of text Long line of text Long line of text Long line of text  Long line of text Long line of text")

    # Test logging output
    # https://docs.python.org/3.9/library/textwrap.html#textwrap.dedent
    detent_text = textwrap.dedent("""\
    Test title
    
    🌲 Item 1     $200,00
    🔻 Item 2     $12,123
    """)
    logger.info(detent_text)

    long_lines_text = textwrap.dedent("""\
    A test with long lines in the content
    
    🌲 Item 1     $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00
    🔻 Item 2     $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123 $12,123
    
            https://tradingstrategy.ai/trading-view
            https://tradingstrategy.ai/blog 
    """)
    logger.info(long_lines_text)

    logger.info("Line of text")

    logger.debug("Debug message %d %d", 1, 2)
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")

    logger.info("Short info message with a link https://tradingstrategy.ai")

    try:
        raise RuntimeError("A bloody exception")
    except Exception as e:
        logger.exception(e)

    # Switch to a handler with emojis
    discord_handler_with_emojis = DiscordHandler("My server log example", webhook_url)
    logger.removeHandler(discord_handler)
    logger.addHandler(discord_handler_with_emojis)
    logger.error("Error output with emojis")
    logger.warning("Warning output with emojis")
    logger.info("Info output with emojis")
    logger.error("Error output with emojis with long message $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00 $200,00")
    logger.error("Error output with emojis\nmultiline")

    # Switch to a handler one with a break character
    discord_handler_with_emojis = DiscordHandler("My server log example", webhook_url, message_break_char="…")
    logger.removeHandler(discord_handler)
    logger.addHandler(discord_handler_with_emojis)
    logger.info("Message 1 … Message 2 … Message 3")


if __name__ == "__main__":
    # Run a manual test
    import os
    webhook_url = os.environ["DISCORD_TEST_WEBHOOK_URL"]
    log_examples(webhook_url)