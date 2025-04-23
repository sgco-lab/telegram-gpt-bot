from modules.gpt import ask_gpt
from modules.loader import load_context
from telebot import TeleBot
import os
import threading
from flask import Flask

# توکن تلگرام و کلید GPT از محیط یا به صورت مستقیم
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or "توکن ربات"
bot = TeleBot(BOT_TOKEN)
context = load_context()

# ربات تلگرام به صورت thread جدا اجرا میشه
def run_bot():
    @bot.message_handler(func=lambda message: True)
    def handle(message):
        response = ask_gpt(message.text, context)
        bot.reply_to(message, response)
    
    print("🤖 Bot is running...")
    bot.infinity_polling()

# اجرای ربات
threading.Thread(target=run_bot).start()

# ساخت وب‌سرور Flask ساده برای Render
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Telegram GPT bot is alive."

# اجرای Flask روی پورت مناسب Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
