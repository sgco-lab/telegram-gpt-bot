import os
import openai

# گرفتن کلید از متغیر محیطی
openai.api_key = os.getenv("OPENAI_API_KEY")

# تابع درخواست به GPT
def ask_gpt(user_input, context="شما یک دستیار هوشمند هستید."):
    try:
        messages = [
            {"role": "system", "content": context},
            {"role": "user", "content": user_input}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        return response["choices"][0]["message"]["content"]
    
    except Exception as e:
        print("❌ خطا در اتصال به GPT:", e)
        return "❌ خطا در پاسخ‌دهی هوش مصنوعی."
