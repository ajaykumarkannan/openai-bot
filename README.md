# README

The code is hosted on [GitHub](https://github.com/ajaykumarkannan/openai-bot/).

This is a simple telegram and discord bot that can use the OpenAI GPT engine.

## Setup and Usage

```bash
# Clone this repository:
git clone https://github.com/ajaykumarkannan/openai-bot/
cd openai-bot

# Install the pip dependencies
pip install -r requirements.txt
touch keys.py
```

First, you'll need to set a file called keys.py with the following content:

```python
openai_api_key = "<openai_api_key>"
telegram_bot_key = "<telegram_bot_key>"
discord_key = '<discord_bot_key>'
sd_key = "<dreamstudio_key>"
```

Make sure to keep your keys in `keys.py` a secret.

Now you're ready to get going. You can either run the telegram bot or the discord bot or both!

```bash
# To run a simple CLI chat bot:
./chatbot.py

# To run the telegram bot:
./telegram_chatbot.py

# To run the discord bot:
./discord_chatbot.py
```

## OpenAI

You can read about OpenAI [here](https://openai.com/api/). There are a lot of parameters and models that you can customize. I'm setting some basic ones, that may change, and I may provide options for.

## Telegram

Use [BotFather](https://t.me/BotFather) to setup your telegram bot.
You will get an authorzation token from it that you can add to your keys.py file.

Once you add the bot to your chat server, you can use the `/p` or `/prompt` command followed by your input to get a response.

### Stable Diffusion

The telegram bot also supports the stable diffusion API to generate images with the default parameters.
It relies on [DreamStudio.AI](https://beta.dreamstudio.ai/).

You can use it like so:

```
/s <prompt for stable diffusion>
```

The bot will respond to your text with an image.

## Discord

Discord was slightly more involved to setup and add to your channels.
You can set up an app and a bot [here](https://discord.com/developers/applications) but look up any tutorials to create one.

Add the bot to a specfic channel and give message permisisons.
Use `/p` at the start of your message to get the bot to respond.
