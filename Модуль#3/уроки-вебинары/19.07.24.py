# import telebot

# from weather import current_weather # импортируем данные из файла weather.py

# Token = 'бот отец'
# bot = telebot.TeleBot(Token)

# @bot.message_handler(commands=['start'])
# def text(message):
#   text = '*полужирный* _курсив_ __подчеркнутый__ \
#     ~зачеркнутый~ \
#       ||спойлер||\
#         `#строка кода`\
#         ```#блок_кода print()```'
#   bot.send_message(message.chat.id,
#                    text=text,
#                    parse_mode="MarkdownV2")

# Функция для получения данных о погоде
# def get_weather(latitude, longitude):
#     url = f'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&windspeed_unti=ms&timezone=Europe%2FMoscow'
#     response = requests.get(url)
#     data = response.json()
#     return data['current_weather']

# # Функция для получения типа погоды по коду
# def get_weather_type(weather_code):
#     return weather_codes.get(weather_code, 'Unknown weather type')

# Обработчик команды /start
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Добро пожаловать! Используйте команду /weather, чтобы узнать текущую погоду.")

# # Обработчик команды /weather
# @bot.message_handler(commands=['weather'])
# def request_location(message):
#     markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
#     button_geo = telebot.types.KeyboardButton(text="Share location", request_location=True)
#     markup.add(button_geo)
#     bot.send_message(message.chat.id, "Пожалуйста, поделитесь своим местоположением, чтобы получить информацию о погоде.", reply_markup=markup)

# Обработчик геолокации
# @bot.message_handler(content_types=['location'])
# def handle_location(message):
#     if message.location is not None:
#         latitude = message.location.latitude
#         longitude = message.location.longitude
#         weather_data = get_weather(latitude, longitude)
        
#         # Извлечение нужных данных
#         temperature = weather_data['temperature']
#         wind_speed = weather_data['windspeed']
#         wind_direction = weather_data['winddirection']
#         weather_code = weather_data['weathercode']
#         weather_type = get_weather_type(weather_code)
        
#         # Формирование сообщения
#         weather_info = (f"Температура воздуха: {temperature}°C\n"
#                         f"Скорость ветра: {wind_speed} м/с\n"
#                         f"Направление ветра: {wind_direction}°\n"
#                         f"Тип погоды: {weather_type}")
        
#         # Отправка сообщения пользователю
#         bot.send_message(message.chat.id, weather_info)

# Запуск бота
# bot.polling(none_stop=True)
