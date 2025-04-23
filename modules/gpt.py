import requests
import os
from utils.embedder import Embedder

# استفاده از کلید API برای Pawan (سرویس GPT شما)
GPT_API_KEY = os.getenv("GPT_API_KEY") or "pk-uaUosLTWqoAQPzySAYfqHRdARIOeeWaNLRDlmwCzQQUXHdYq"  # مطمئن شوید که کلید واقعی رو قرار می‌دهید
GPT_API_URL = "https://api.pawan.krd/v1/chat/completions"

embedder = Embedder()

def ask_gpt(user_input, context=None):
    try:
        matched = embedder.search(user_input)
        smart_context = "\n".join(matched)
    except:
        smart_context = context or "شما یک ربات پشتیبانی هوشمند هستید."

    headers = {
        "Authorization": f"Bearer {GPT_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # یا مدل‌های دیگر بسته به مستندات API پلتفرم Pawan
        "messages": [
            {"role": "system", "content": smart_context},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(GPT_API_URL, headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print("❌ خطا در ارتباط با API:", e)
        return "❌ خطا در پاسخ‌دهی هوش مصنوعی."
