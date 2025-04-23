import os
import threading
from flask import Flask
from telebot import TeleBot
from gpt import ask_gpt

# توکن ربات تلگرام
BOT_TOKEN = "7364375268:AAHINkpnSsFdOf_gcaedtBw0G95Zj6dLjVE"
bot = TeleBot(BOT_TOKEN)

# context پیش‌فرض (میشه از فایل هم لود کرد)
context = "شما یک ربات پشتیبان فروش هستید. پاسخ دقیق، مؤدب و حرفه‌ای بده."

# اجرای ربات تلگرام در ترد جدا
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

threading.Thread(target=run_bot).start()

# اجرای Flask برای Render (پورت باز)
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ ربات فعال است!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
