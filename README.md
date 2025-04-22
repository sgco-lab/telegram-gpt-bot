# Telegram GPT Support Bot

🤖 A smart Telegram bot for customer support based on PDF instructions, website content, and AI.

## Features

- Connected to GPT (via Pawan API)
- Smart search over product documents using TF-IDF
- Automatic replies to Telegram users
- Supports Persian language
- Embeddable knowledge base

## Deploy to Render

1. Fork this repo or clone it
2. Create a free account at https://render.com
3. Select "New + > Web Service"
4. Connect your GitHub and select this repo
5. Set the following:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
   - **Environment Variables**:
     - `GPT_API_KEY`: your Pawan API key
     - `TELEGRAM_BOT_TOKEN`: your Telegram bot token

Enjoy 24/7 smart support bot for your business 😎
