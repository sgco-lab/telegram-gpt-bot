from telebot import TeleBot
import os
from modules.gpt import ask_gpt

BOT_TOKEN = os.getenv("BOT_TOKEN") or "7364375268:AAHINkpnSsFdOf_gcaedtBw0G95Zj6dLjVE"

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    reply = ask_gpt(user_input)
    bot.reply_to(message, reply)

if __name__ == "__main__":
    bot.remove_webhook()  # خیلی مهمه!
    print("🤖 ربات در حال اجراست (Polling فعال است)...")
    bot.infinity_polling()
