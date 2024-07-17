import requests

r = requests.get('https://cataas.com/cat/says/Привет?json=true')
print(r)

print(r.status_code)

print(r.content)

print(r.json()['_id'])

txt = 'Привет'
print( 'https://cataas.com/cat/' + r.json()['_id'] + f'/says/{txt}')


import requests
import telebot

token = 'токен_ботОтец'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['rand_cat'])
def send_rand_cat(message):
  r = requests.get( 'https://cataas.com/cat?json=true')
  url = 'https://cataas.com/cat/' + r.json()['_id']
  bot. send_photo(message.chat.id, url)

@bot.message_handler(commands=['photo_with_text'])
def photo_with_text(message) :
  msg = bot.send_message(message.chat.id,
                         f'Введите текст')
  bot.register_next_step_handler(msg,
                                 send_random_photo_with_text)

def send_random_photo_with_text(message) : 
  r = requests.get('https://cataas.com/cat/says/' +
                   message.text + '?json=true')
  url = 'https://cataas.com/cat/' + r.json()['_id'] + f'/says/{message.text}'
  bot. send_photo(message.chat.id, url)

@bot.message_handler(commands=['sentiment'])
def start(message):
  msg = bot.send_message(message.chat.id,
                         'Введите текст для оценки')
  bot.register_next_step_handler(msg,
                                 get_sentiment)
def get_sentiment (message): 
  data = {'x': [message.text]}

  res = requests.post('https://7034.deeppavlov.ai/model', json=data).json()
  s = res[0][0]
  bot.send_message(message.chat.id,
                   f'Оценка: {s}')
  
@bot.message_handler(commands=['rand_dog'])
def send_rand_dog (message):
  r = requests.get('https://random.dog/woof.json') 
  url = r.json()['url']
  bot. send_photo(message.chat.id, url)

@bot.message_handler (commands=['rand_duck'])
def send_rand_duck (message):
  r = requests.get('https://random-d.uk/api/random')
  url = r.json()['url']
  bot.send_message(message.chat.id, url)

bot.infinity_polling()

# import requests
# import telebot

# token = 'токен_ботОтец'
# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['rand_cat'])
# def send_rand_cat(message):
#     try:
#         r = requests.get('https://cataas.com/cat?json=true')
#         r.raise_for_status()  # Проверка на успешный запрос
#         url = 'https://cataas.com/cat/' + r.json()['_id']
#         bot.send_photo(message.chat.id, url)
#     except Exception as e:
#         bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

# @bot.message_handler(commands=['photo_with_text'])
# def photo_with_text(message):
#     msg = bot.send_message(message.chat.id, 'Введите текст')
#     bot.register_next_step_handler(msg, send_random_photo_with_text)

# def send_random_photo_with_text(message):
#     try:
#         r = requests.get('https://cataas.com/cat/says/' + message.text + '?json=true')
#         r.raise_for_status()  # Проверка на успешный запрос
#         url = 'https://cataas.com/cat/' + r.json()['_id'] + f'/says/{message.text}'
#         bot.send_photo(message.chat.id, url)
#     except Exception as e:
#         bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

# @bot.message_handler(commands=['sentiment'])
# def start(message):
#     msg = bot.send_message(message.chat.id, 'Введите текст для оценки')
#     bot.register_next_step_handler(msg, get_sentiment)

# def get_sentiment(message):
#     try:
#         data = {'x': [message.text]}
#         res = requests.post('https://7034.deeppavlov.ai/model', json=data).json()
#         s = res[0][0]  # Если возвращает список списков
#         bot.send_message(message.chat.id, f'Оценка: {s}')
#     except Exception as e:
#         bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

# @bot.message_handler(commands=['rand_dog'])
# def send_rand_dog(message):
#     try:
#         r = requests.get('https://random.dog/woof.json')
#         r.raise_for_status()  # Проверка на успешный запрос
#         url = r.json()['url']
#         bot.send_photo(message.chat.id, url)
#     except Exception as e:
#         bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

# @bot.message_handler(commands=['rand_duck'])
# def send_rand_duck(message):
#     try:
#         r = requests.get('https://random-d.uk/api/random')
#         r.raise_for_status()  # Проверка на успешный запрос
#         url = r.json()['url']
#         bot.send_message(message.chat.id, url)
#     except Exception as e:
#         bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

# bot.infinity_polling()
