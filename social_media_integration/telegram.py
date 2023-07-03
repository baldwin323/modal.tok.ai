```python
import telebot
from telebot import types
from natural_language_processing.nltk import process_message
from api_backend.onlyfans_affiliate import track_referral
from payment_system.payment import process_payment

# Obtain your token from @BotFather
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Model Talk AI!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_message = message.text
    response = process_message(user_message)
    bot.reply_to(message, response)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if 'buy' in message.text.lower():
        process_payment(message.chat.id, message.text)
        bot.reply_to(message, "Thank you for your purchase!")
    elif 'referral' in message.text.lower():
        track_referral(message.chat.id, message.text)
        bot.reply_to(message, "Referral tracked. Thank you!")

bot.polling()
```