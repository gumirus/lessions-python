import telebot

from weather import current_weather # импортируем данные из файла weather.py

Token = '6835062044:AAFsRbl5CGo-NsgblLrLQpCQMCcH8G0bsIE'
bot = telebot.TeleBot(Token)

#Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message, "Добро пожаловать! Используйте команду /weather, чтобы узнать текущую погоду.")

@bot.message_handler(commands=['weather'])
def weather(message):
  keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1,
                                               resize_keyboard=True)
  button_geo = telebot.types.KeyboardButton(text='Поделиться местоположением',
                                            request_location=True)
  keyboard.add(button_geo)
  bot.send_message(message.chat.id,
                   'Поделитесь местоположением',
                   reply_markup=keyboard)
@bot.message_handler(content_types=['location'])
def location(message):
  a = telebot.types.ReplyKeyboardRemove()
  bot.send_message(message.chat.id,
                   current_weather(message.location.latitude,
                                   message.location.longitude),
                                   reply_markup=a)
bot.infinity_polling()
