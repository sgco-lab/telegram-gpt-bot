import telebot

BOT_TOKEN = "7364375268:AAHINkpnSsFdOf_gcaedtBw0G95Zj6dLjVE"
bot = telebot.TeleBot(BOT_TOKEN)

updates = bot.get_updates()
print("✅ اتصال موفق. تعداد پیام‌ها:", len(updates))
