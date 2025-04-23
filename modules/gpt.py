import requests
import os
from utils.embedder import Embedder

# 📌 توکن API از پلتفرم پوان کرُد
GPT_API_KEY = os.getenv("pk-uaUosLTWqoAQPzySAYfqHRdARIOeeWaNLRDlmwCzQQUXHdYq") or "pk-uaUosLTWqoAQPzySAYfqHRdARIOeeWaNLRDlmwCzQQUXHdYq"

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
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": smart_context},
            {"role": "user", "content": user_input}
        ]
    }

        try:
        response = requests.post(GPT_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print("❌ خطا در ارتباط با GPT API:", e)
        print("⛔ پاسخ سرور:", response.text)
        return "❌ خطا در پاسخ‌دهی هوش مصنوعی."

