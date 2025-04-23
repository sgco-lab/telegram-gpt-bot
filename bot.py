import os
import threading
from flask import Flask
from telebot import TeleBot, types
from modules.gpt import ask_gpt
from modules.loader import load_context

# ✅ توکن ربات تلگرام
BOT_TOKEN = "7364375268:AAHINkpnSsFdOf_gcaedtBw0G95Zj6dLjVE"  # حتماً درست و بدون فاصله بذار

# 🎯 اتصال به بات
bot = TeleBot(BOT_TOKEN)
context = load_context()

# 🚫 جلوگیری از خطای 409
bot.remove_webhook()

# ✅ اجرای بات با Polling در ترد جداگانه
def run_bot():
    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        try:
            response = ask_gpt(message.text, context)
            bot.reply_to(message, response)
        except Exception as e:
            print("❌ خطا:", e)
            bot.reply_to(message, "خطا در پاسخ‌دهی هوش مصنوعی.")

    print("🤖 ربات در حال اجراست (Polling فعال است)...")
    bot.remove_webhook()  # جلوگیری از خطای 409 - خاموش کردن webhook
    bot.infinity_polling()

# 🚀 اجرای ترد برای Polling
threading.Thread(target=run_bot).start()

# 🌐 ساخت اپ Flask برای Render
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ ربات تلگرام GPT فعال است."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
