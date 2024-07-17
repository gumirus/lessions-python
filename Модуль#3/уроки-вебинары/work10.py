# import telebot

# token = ''

# bot = telebot.TeleBot(token)

# @bot.message_handler(content_types=['sticker'])
# def get_sticker(message):
#     bot.send_message(message.chat.id, f'ID твоего стикера - {message.sticker.file_id}')

# @bot.message_handler(content_types=['pinned_message'])
# def pin(message):
#     bot.send_message(message.chat.id, f'{message.from_user.username} опять что-то закрепил')

# @bot.message_handler(content_types=['photo', 'document'])
# def get_photo_or_doc(message):
#     bot.send_message(message.chat.id, f'Я получил что-то важное')

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, f'Добрый день, {message.from_user.first_name}!')

# @bot.message_handler(commands=['get_info'])
# def get_info(message):
#     send = bot.send_message(message.chat.id,
#     '''Что именно вы хотите узнать?\n
# first_name - Ваше\nusername - Ваш ник\nlast_name - Ваша фамилия''')
#     bot.register_next_step_handler(send, info)

# def info(message):
#     try:
#         if message.text == 'first_name':
#             bot.send_message(message.chat.id, message.from_user.first_name)
#         elif message.text == 'username':
#             bot.send_message(message.chat.id, message.from_user.username)
#         elif message.text == 'last_name':
#             bot.send_message(message.chat.id, message.from_user.last_name)
#         else:
#             bot.send_message(message.chat.id, 'Я такого не знаю')
#     except:
#         bot.send_message(message.chat.id, 'Данные не указаны')
# @bot.message_handler(commands=['help'])
# def help(message):
#     text = ''''''

# bot.infinity_polling()

# import telebot

# TOKEN = ''

# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(content_types=['text'])
# def echo(message):
#     if message.text.lower() in ['привет']:
#         bot.send _message(message.chat.id,
#                            'Привет' )
#     else:
#         bot.send_message(message.chat.id, message.text)

# @bot.message_handler(func = lambda x: x.text.lower() in ['привет'])
# def say(message):
#   bot.send_message(message.chat.id,'Привет')

# @bot.message_handler(content_types=['text'])
# def echo(message):
#   bot.send_message(message.chat.id, message.text)


import telebot

Token = ''

bot = telebot.TeleBot(Token)

to_do = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'''Добрый день, 
                     {message.from_user.username}!\nВаш список дел сгенерирован.''')
    to_do[message.from_user.username] = {
        'Понедельник': [],
        'Вторник': [],
        'Среда': [], 
        'Четверг': [], 
        'Пятница': [],
        'Суббота': [],
        'Воскресенье': []
    }

@bot.message_handler(commands=['add'])
def add(message):
    msg = bot.send_message(message.chat.id, 'Введите день недели для добавления дела')
    bot.register_next_step_handler(msg, dw_for_add)

def dw_for_add(message):
    if message.text.capitalize() in to_do[message.from_user.username]:
        msg = bot.send_message(message.chat.id, 'Введите дело')
        bot.register_next_step_handler(msg, add_to_dict, message.text.capitalize())
    else:
        bot.send_message(message.chat.id, 'Такого дня недели не существует')

def add_to_dict(message, day):
    to_do[message.from_user.username][day].append(message.text)
    bot.send_message(message.chat.id, 'Готово')

@bot.message_handler(commands=['print'])
def print_to_do_list(message):
    text = ""
    for day in to_do[message.from_user.username]:
        text += f'\nСписок дел на {day}:\n'
        if to_do[message.from_user.username][day]:
            text += '\n'.join(str(i) for i in to_do[message.from_user.username][day]) + '\n'
        else:
            text += 'Нет дел\n'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать работу с ботом и сгенерировать список дел\n"
        "/add - Добавить дело в список\n"
        "/print - Показать список дел\n"
        "/help - Показать это сообщение"
    )
    bot.send_message(message.chat.id, help_text)

bot.infinity_polling()
