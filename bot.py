import os
from dotenv import load_dotenv
import telebot

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: (
    message.text is not None and 
    message.text.strip().isdigit() and 
    1 <= len(message.text.strip()) <= 9
))
def forward_postback_message(message):
    # Если сообщение состоит только из цифр нужной длины, отправляем его в канал
    bot.send_message(CHAT_ID, message.text.strip())

bot.infinity_polling(timeout=60, long_polling_timeout=30)