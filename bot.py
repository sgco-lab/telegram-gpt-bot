import os
import threading
from flask import Flask
from telebot import TeleBot
from modules.gpt import ask_gpt
from modules.loader import load_context

# --- تنظیمات اولیه ---
BOT_TOKEN = "7364375268:AAHINkpnSsFdOf_gcaedtBw0G95Zj6dLjVE"
bot = TeleBot(BOT_TOKEN)
context = load_context()

# حذف webhook برای جلوگیری از ارور 409
bot.remove_webhook()

# --- تابع اجرای ربات تلگرام ---
def run_bot():
    @bot.message_handler(func=lambda message: True)
    def handle(message):
        try:
            response = ask_gpt(message.text, context)
            bot.reply_to(message, response)
        except Exception as e:
            print("❌ خطا:", e)
            bot.reply_to(message, "❌ خطا در پاسخ‌دهی هوش مصنوعی.")

    print("🤖 ربات در حال اجراست (Polling فعال است)...")
    bot.infinity_polling(skip_pending=True)  # پیام‌های قدیمی رو رد کن

# اجرای ربات در یک Thread جدا برای هماهنگی با Flask
threading.Thread(target=run_bot).start()

# --- اپلیکیشن Flask برای نگه داشتن پروژه فعال در Render ---
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ ربات آنلاین و فعال است!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
