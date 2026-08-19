# Discord.py Template

A small starter template for building Discord bots with Python and `discord.py`. It includes slash commands and examples of buttons, dropdown menus, and modal forms.

## Features

- Slash commands using `client.tree.command`
- Automatic slash-command synchronization on startup
- Interactive buttons
- Dropdown/select menus
- Modal forms with text inputs
- Separate modules for reusable UI components

## Requirements

- Python 3.10 or newer
- A Discord application and bot token
- A test Discord server where you can install the bot

The pinned dependencies are listed in [requirements.txt](requirements.txt).

## Installation

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

2. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Create a bot in the [Discord Developer Portal](https://discord.com/developers/applications).

4. Invite the bot to a server with the required scopes and permissions:

   - `bot`
   - `applications.commands`

5. Store the bot token in an environment variable named `DISCORD_TOKEN`.

   Windows PowerShell:

   ```powershell
   $env:DISCORD_TOKEN = "your-bot-token"
   ```

   macOS/Linux:

   ```bash
   export DISCORD_TOKEN="your-bot-token"
   ```

6. Run the bot:

   ```bash
   python template.py
   ```

   The duplicate project copy can be run with:

   ```bash
   python discord.py_template/main.py
   ```

## Available Commands

After the bot starts and synchronizes its application commands, the template provides:

| Command | Description |
| --- | --- |
| `/hello` | Greets the command user, or a selected server member. |
| `/modal` | Opens the example modal form. |
| `/button` | Displays an ephemeral message with a green button. |
| `/dropdown` | Displays an ephemeral colour-selection dropdown. |

## Project Structure

```text
.
├── template.py                 # Main bot example
├── requirements.txt            # Pinned Python dependencies
├── setup.txt                   # Basic setup notes
├── buttons/button.py           # Button view example
├── dropdowns/dropdown.py       # Dropdown view example
├── modals/modal.py             # Modal form example
└── discord.py_template/        # Duplicate, more heavily commented copy
```

## Customization

- Add new slash commands with `@client.tree.command(...)`.
- Put reusable buttons, selects, and modals in the corresponding component directories.
- The examples use `discord.Intents.default()` because these slash commands do not need privileged intents.
- Add error handling and permission checks before deploying publicly.

## Important Security Notes

Never commit a bot token to source control or paste it into a public repository. If a token was previously exposed in these files or in git history, revoke and regenerate it immediately in the Discord Developer Portal, then load the replacement from `DISCORD_TOKEN` or another secret manager.

Also add local secret files to `.gitignore`, for example:

```gitignore
.env
.venv/
__pycache__/
```

## API Documentation

- [discord.py documentation](https://discordpy.readthedocs.io/en/stable/)
- [discord.py API reference](https://discordpy.readthedocs.io/en/stable/api.html)
- [discord.py application commands](https://discordpy.readthedocs.io/en/stable/interactions/api.html)
- [discord.py UI components](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui)
- [Discord Developer Documentation](https://discord.com/developers/docs/intro)
- [Discord Application Commands](https://discord.com/developers/docs/interactions/application-commands)
- [Discord Interactions](https://discord.com/developers/docs/interactions/receiving-and-responding)
- [Discord Gateway intents](https://discord.com/developers/docs/events/gateway#gateway-intents)
- [Discord OAuth2 URL generator](https://discord.com/developers/docs/topics/oauth2)

## License

No license has been specified for this template.
