import os
import threading
from flask import Flask
from telebot import TeleBot
from modules.gpt import ask_gpt
from modules.loader import load_context

# توکن ربات از محیط یا مستقیم
BOT_TOKEN = os.getenv("7796045738:AAFcvuZxBD_3nUirM61gAEPQxDWpoO8gBFo") or "توکن ربات شما"
bot = TeleBot(BOT_TOKEN)
context = load_context()

# اجرای ربات تلگرام در یک ترد جدا
def run_bot():
    @bot.message_handler(func=lambda message: True)
    def handle(message):
        try:
            response = ask_gpt(message.text, context)
            bot.reply_to(message, response)
        except Exception as e:
            print("❌ خطا:", e)
            bot.reply_to(message, "خطا در پاسخ‌دهی هوش مصنوعی.")

    print("🤖 ربات در حال اجراست...")
    bot.infinity_polling()

# اجرا کردن ربات در بک‌گراند
threading.Thread(target=run_bot).start()

# سرور Flask ساده فقط برای نگه داشتن پورت باز
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ ربات هوش مصنوعی تلگرام فعاله!"

# اجرای سرور Flask برای اینکه Render پورت رو شناسایی کنه
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
