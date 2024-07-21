import requests
import telebot

# Приписываем токен_ботОтец
token = 'токен_ботОтец'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message, "Добро пожаловать! Используйте команду /coffee, чтобы узнать текущую погоду.")

@bot.message_handler(commands=['coffee'])
def send_coffee_photo(message):    
    """
     Приписываем команду /coffee в телеграмм и бот должен 
     отправлять рандомное фото из интернета JSON.
    """

    r = requests.get('https://coffee.alexflipnote.dev/random.json')
    url = r.json()['file']
    bot.send_photo(message.chat.id, url)

# Запуск бота
bot.infinity_polling()
