# 0.1.5

- Fix: Discord rate limiting issues. When sending too frequent logs, Discord starts to throttle with HTTP 429
  code and that might have caused the logger to trip into an infinite loop.

# 0.1.4

- Update to `discord-webhook` version 1.0.0 

# 0.1.3

- More error diagnostics output in the case of Discord server rejects our message 

# 0.1.2

- Add `discord_timeout` with default 5 seconds value

# 0.1.1

- Fix package metadata and README on PyPi

# 0.1

- Initial release
