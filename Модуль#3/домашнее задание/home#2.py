import telebot
import random
import re

Token = 'токен от телеграм ботОтец'

bot = telebot.TeleBot(Token)

# хэндлер слово "рандом"
@bot.message_handler(func=lambda message: re.search(r'рандом', message.text, re.IGNORECASE))
def send_random_number(message):
    random_number = random.randint(0, 100)
    bot.reply_to(message, str(random_number))

# хэндлер для всех остальных
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)

