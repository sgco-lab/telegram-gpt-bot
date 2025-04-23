import os
import threading
from flask import Flask
from telebot import TeleBot
from modules.gpt import ask_gpt
from modules.loader import load_context

# توکن ربات تلگرام
BOT_TOKEN = "7364375268:AAHINkpnSsFdOf_gcaedtBw0G95Zj6dLjVE"
bot = TeleBot("7364375268:AAHINkpnSsFdOf_gcaedtBw0G95Zj6dLjVE")
context = load_context()

# اجرای ربات تلگرام در یک ترد جداگانه
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
    bot.infinity_polling()  # استفاده از polling برای دریافت پیام‌ها

# اجرای ترد ربات
threading.Thread(target=run_bot).start()

# ساخت سرور Flask ساده برای Render
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ ربات فعال است!"

if __name__ == "__main__":
    # پورت را از متغیر محیطی یا مقدار پیش‌فرض استفاده می‌کنیم
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
