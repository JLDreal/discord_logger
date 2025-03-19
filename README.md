# Discord Message Logger Bot

This is a simple Discord bot that logs messages from channels to a SQLite database. It captures the date, time, server name, channel, user, and message content for each message sent in the server.

## Features

- Logs messages to a SQLite database.
- Captures the following information:
  - Date and time of the message
  - Server name
  - Channel name
  - User who sent the message
  - Message content
- Ignores messages sent by the bot itself to prevent infinite loops.

## Requirements

- Python 3.6 or higher
- `discord.py` library
- SQLite (comes pre-installed with Python)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/discord-message-logger.git
   cd discord-message-logger
   ```

2. **Install the required libraries:**

   You can install the `discord.py` library using pip:

   ```bash
   pip install discord.py
   ```

3. **Set up your Discord bot:**

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and add a bot to it.
   - Copy the bot token.

4. **Set the bot token:**

5. **Run the bot:**

   ```bash
   python dc_log.py
   ```

## Usage

Once the bot is running, it will log messages from any channel it has access to in the server. The messages will be stored in a SQLite database located at `~/Dokumente/messages.db`.

## Database Structure

The SQLite database will have a table named `messages` with the following columns:

- `date` (TEXT): The date when the message was sent.
- `time` (TEXT): The time when the message was sent.
- `server_name` (TEXT): The name of the server where the message was sent.
- `channel` (TEXT): The name of the channel where the message was sent.
- `user` (TEXT): The user who sent the message.
- `message` (TEXT): The content of the message.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the GPL License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [discord.py](https://discordpy.readthedocs.io/en/stable/) - The library used to interact with the Discord API.
