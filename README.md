# Discord-User-AI

This readme file was made with the discord ai 💀

Turn your Discord account into an AI-powered chatbot using Google's Gemini AI. This script automatically replies to messages in a specified Discord channel, enabling your account to respond as if it's an intelligent AI assistant.

## Features

- Automated replies powered by Google's Gemini AI (Gemini 1.5-Flash)
- Simple configuration and setup
- Avoids replying to its own messages
- Adjustable polling rate to match your server's cooldown

## Requirements

- Python 3.x installed
- Discord Account Token
- Google Gemini API Key (Free)

## Setup Instructions

### 1. Install Dependencies

Run the following command to install the required Python libraries:

```bash
pip install requests urllib3 httpx
```

### 2. Obtain Discord Token and IDs

- **Discord Token:** Retrieve your Discord token using developer tools or external tools.
- **Channel ID & Guild ID:** Enable developer mode in Discord settings (`User Settings -> Advanced -> Developer Mode`) then right-click on your channel and server to copy their IDs.
- **User ID:** Right-click your username and copy your user ID (prevents the bot from replying to itself).

### 3. Obtain Google Gemini API Key

Visit [Google AI Studio](https://aistudio.google.com/apikey) and generate a free Gemini API Key.

### 4. Configuration

Replace placeholders in the script with your own:

```python
TOKEN = "YOUR_DISCORD_TOKEN"
CHANNEL = "YOUR_CHANNEL_ID"
GUILD = "YOUR_SERVER_ID"
GEMINI_KEY = "YOUR_GEMINI_API_KEY"
YourUserID = "YOUR_USER_ID"
```

### 5. Run the Script

Execute the script with Python:

```bash
python yourscript.py
```

Your Discord account will now automatically reply to new messages in the selected channel.

## Important Notes

- Ensure your account has permission to send messages in the target Discord channel.
- Keep your Discord token private to prevent unauthorized access to your account.
- Adjust `time.sleep(5)` to fit the channel's cooldown requirements.

## Credits

- Created by **PotatoIsCool**
- Powered by [Google Gemini AI](https://aistudio.google.com)

Enjoy making your Discord account AI-powered! 🚀

