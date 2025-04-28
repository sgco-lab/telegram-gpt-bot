import os
from flask import Flask, request
from telebot import TeleBot, types
from modules.gpt import ask_gpt

# گرفتن توکن ربات از متغیر محیطی
BOT_TOKEN = os.getenv("7663649749:AAGQtMWCY3hrNtczlqtzY9Xldf1ydmaoBG4")
bot = TeleBot(BOT_TOKEN)

# context پیش‌فرض
context = "شما یک ربات پشتیبان فروش هستید. پاسخ دقیق، مؤدب و حرفه‌ای بده."

# ساخت اپ Flask
app = Flask(__name__)

# مسیری که Telegram پیام‌های جدید را به آن POST می‌کند
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = types.Update.de_json(json_str, bot)
    try:
        response = ask_gpt(update.message.text, context)
        bot.reply_to(update.message, response)
    except Exception as e:
        print("❌ خطا:", e)
        bot.reply_to(update.message, "خطا در پاسخ‌دهی هوش مصنوعی.")
    return 'OK', 200

# مسیر اصلی برای چک سلامت
@app.route('/')
def index():
    return "✅ ربات فعال است!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    bot.remove_webhook()
    app_url = os.environ.get('https://telegram-gpt-bot-si8h.onrender.com')  # مثلا: https://your-app-name.onrender.com
    bot.set_webhook(url=f"{app_url}/{BOT_TOKEN}")
    app.run(host="0.0.0.0", port=port)
import os
from flask import Flask, request
from telebot import TeleBot, types
from modules.gpt import ask_gpt

# گرفتن توکن ربات از متغیر محیطی
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(BOT_TOKEN)

# context پیش‌فرض
context = "شما یک ربات پشتیبان فروش هستید. پاسخ دقیق، مؤدب و حرفه‌ای بده."

# ساخت اپ Flask
app = Flask(__name__)

# مسیری که Telegram پیام‌های جدید را به آن POST می‌کند
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = types.Update.de_json(json_str, bot)
    try:
        response = ask_gpt(update.message.text, context)
        bot.reply_to(update.message, response)
    except Exception as e:
        print("❌ خطا:", e)
        bot.reply_to(update.message, "خطا در پاسخ‌دهی هوش مصنوعی.")
    return 'OK', 200

# مسیر اصلی برای چک سلامت
@app.route('/')
def index():
    return "✅ ربات فعال است!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    bot.remove_webhook()
    app_url = os.environ.get('APP_URL')  # مثلا: https://your-app-name.onrender.com
    bot.set_webhook(url=f"{app_url}/{BOT_TOKEN}")
    app.run(host="0.0.0.0", port=port)
import os
from flask import Flask, request
from telebot import TeleBot, types
from modules.gpt import ask_gpt

# گرفتن توکن ربات از متغیر محیطی
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(BOT_TOKEN)

# context پیش‌فرض
context = "شما یک ربات پشتیبان فروش هستید. پاسخ دقیق، مؤدب و حرفه‌ای بده."

# ساخت اپ Flask
app = Flask(__name__)

# مسیری که Telegram پیام‌های جدید را به آن POST می‌کند
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = types.Update.de_json(json_str, bot)
    try:
        response = ask_gpt(update.message.text, context)
        bot.reply_to(update.message, response)
    except Exception as e:
        print("❌ خطا:", e)
        bot.reply_to(update.message, "خطا در پاسخ‌دهی هوش مصنوعی.")
    return 'OK', 200

# مسیر اصلی برای چک سلامت
@app.route('/')
def index():
    return "✅ ربات فعال است!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    bot.remove_webhook()
    app_url = os.environ.get('APP_URL')  # مثلا: https://your-app-name.onrender.com
    bot.set_webhook(url=f"{app_url}/{BOT_TOKEN}")
    app.run(host="0.0.0.0", port=port)
import os
from flask import Flask, request
from telebot import TeleBot, types
from modules.gpt import ask_gpt

# گرفتن توکن ربات از متغیر محیطی
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(BOT_TOKEN)

# context پیش‌فرض
context = "شما یک ربات پشتیبان فروش هستید. پاسخ دقیق، مؤدب و حرفه‌ای بده."

# ساخت اپ Flask
app = Flask(__name__)

# مسیری که Telegram پیام‌های جدید را به آن POST می‌کند
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = types.Update.de_json(json_str, bot)
    try:
        response = ask_gpt(update.message.text, context)
        bot.reply_to(update.message, response)
    except Exception as e:
        print("❌ خطا:", e)
        bot.reply_to(update.message, "خطا در پاسخ‌دهی هوش مصنوعی.")
    return 'OK', 200

# مسیر اصلی برای چک سلامت
@app.route('/')
def index():
    return "✅ ربات فعال است!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    bot.remove_webhook()
    app_url = os.environ.get('APP_URL')  # مثلا: https://your-app-name.onrender.com
    bot.set_webhook(url=f"{app_url}/{BOT_TOKEN}")
    app.run(host="0.0.0.0", port=port)
import os
from flask import Flask, request
from telebot import TeleBot, types
from modules.gpt import ask_gpt

# گرفتن توکن ربات از متغیر محیطی
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(BOT_TOKEN)

# context پیش‌فرض
context = "شما یک ربات پشتیبان فروش هستید. پاسخ دقیق، مؤدب و حرفه‌ای بده."

# ساخت اپ Flask
app = Flask(__name__)

# مسیری که Telegram پیام‌های جدید را به آن POST می‌کند
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = types.Update.de_json(json_str, bot)
    try:
        response = ask_gpt(update.message.text, context)
        bot.reply_to(update.message, response)
    except Exception as e:
        print("❌ خطا:", e)
        bot.reply_to(update.message, "خطا در پاسخ‌دهی هوش مصنوعی.")
    return 'OK', 200

# مسیر اصلی برای چک سلامت
@app.route('/')
def index():
    return "✅ ربات فعال است!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    bot.remove_webhook()
    app_url = os.environ.get('APP_URL')  # مثلا: https://your-app-name.onrender.com
    bot.set_webhook(url=f"{app_url}/{BOT_TOKEN}")
    app.run(host="0.0.0.0", port=port)
import os
from flask import Flask, request
from telebot import TeleBot, types
from modules.gpt import ask_gpt

# گرفتن توکن ربات از متغیر محیطی
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(BOT_TOKEN)

# context پیش‌فرض
context = "شما یک ربات پشتیبان فروش هستید. پاسخ دقیق، مؤدب و حرفه‌ای بده."

# ساخت اپ Flask
app = Flask(__name__)

# مسیری که Telegram پیام‌های جدید را به آن POST می‌کند
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = types.Update.de_json(json_str, bot)
    try:
        response = ask_gpt(update.message.text, context)
        bot.reply_to(update.message, response)
    except Exception as e:
        print("❌ خطا:", e)
        bot.reply_to(update.message, "خطا در پاسخ‌دهی هوش مصنوعی.")
    return 'OK', 200

# مسیر اصلی برای چک سلامت
@app.route('/')
def index():
    return "✅ ربات فعال است!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    bot.remove_webhook()
    app_url = os.environ.get('APP_URL')  # مثلا: https://your-app-name.onrender.com
    bot.set_webhook(url=f"{app_url}/{BOT_TOKEN}")
    app.run(host="0.0.0.0", port=port)
