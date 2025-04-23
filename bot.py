import os
from flask import Flask, request
from telebot import TeleBot, types
from modules.gpt import ask_gpt
from modules.loader import load_context

BOT_TOKEN = "7364375268:AAHINkpnSsFdOf_gcaedtBw0G95Zj6dLjVEا"
bot = TeleBot(BOT_TOKEN)
context = load_context()

WEBHOOK_URL = os.getenv("WEBHOOK_URL") or "https://نام-سرویس-تو-on-render.onrender.com/webhook"

# حذف webhook قبلی و تنظیم جدید
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(func=lambda m: True)
def handle(message):
    try:
        response = ask_gpt(message.text, context)
        bot.reply_to(message, response)
    except Exception as e:
        print("❌ خطا:", e)
        bot.reply_to(message, "خطا در پاسخ‌دهی هوش مصنوعی.")

@app.route("/")
def home():
    return "✅ ربات فعال است!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
