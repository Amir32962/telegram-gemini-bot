import telebot
import requests
import os

# 🔑 گرفتن توکن‌ها از متغیر محیطی (توی Railway ست می‌کنی)
TELEGRAM_TOKEN = os.getenv("8231811220:AAE3nW76_QMhVwD_0r_gnxajCcYpe8aZWq8")
GEMINI_API_KEY = os.getenv("AIzaSyC7EI4jNCO_8yPgxHtnleAoLdbMys-an1M")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# تابع پرسش از Gemini
def ask_gemini(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers=headers, params=params, json=data)
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

# هندل همه پیام‌ها
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        reply = ask_gemini(message.text)
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"❌ خطا: {e}")

print("🤖 Bot is running ...")
bot.polling()
