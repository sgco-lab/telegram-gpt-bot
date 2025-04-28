import os
import requests

API_URL = "https://platform.krd/v1/chat/completions"
API_KEY = os.getenv("API_KEY")  # از متغیر محیطی صحیح خوانده شود

def ask_gpt(message, context):
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": context},
                {"role": "user", "content": message}
            ]
        }

        response = requests.post(API_URL, headers=headers, json=data)

        # چک کردن موفقیت درخواست
        if response.status_code != 200:
            print("❌ خطا در پاسخ از API:", response.text)
            return "خطا در ارتباط با سرور هوش مصنوعی."

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        print("❌ خطا در اتصال به GPT:", e)
        return "خطا در پاسخ‌دهی هوش مصنوعی."
