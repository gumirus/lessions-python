import telebot
import random

Token = 'токен ботОтец'

bot = telebot.TeleBot(Token)

# Основное приветствие
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Используйте команду /start1, /start2, /reply, /game.")

# Команда /start1 с кнопкой
@bot.message_handler(commands=['start1'])
def start1(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text="Нажми меня!", callback_data="button1")
    markup.add(button)
    bot.send_message(message.chat.id, "Нажми на кнопку", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'button1')
def callback(call):
    bot.answer_callback_query(call.id, 'Вы нажали кнопку 1')

# Команда /reply с клавиатурой
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add('Кнопка 1', 'Кнопка 2', 'Кнопка 3')

@bot.message_handler(commands=['reply'])
def start_reply(message):
    bot.send_message(message.chat.id, 'Привет, это тестовый бот!', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in ['Кнопка 1', 'Кнопка 2', 'Кнопка 3'])
def echo_message(message):
    if message.text == 'Кнопка 1':
        bot.reply_to(message, 'Вы нажали кнопку 1')
    elif message.text == 'Кнопка 2':
        bot.reply_to(message, 'Вы нажали кнопку 2')
    elif message.text == 'Кнопка 3':
        bot.reply_to(message, 'Вы нажали кнопку 3')

# Команда /game для игры "Камень, Ножницы, Бумага"
ans = ['Камень', 'Ножницы', 'Бумага']

@bot.message_handler(commands=['game'])
def start_game(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for i in ans:
        keyboard.add(telebot.types.InlineKeyboardButton(text=i, callback_data=i))
    bot.send_message(message.chat.id, 'Что выберешь?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ans)
def callback_query(call):
    user_move = call.data
    bot_move = random.choice(ans)
    bot.send_message(call.message.chat.id, f'Ты выбрал {user_move}')
    bot.send_message(call.message.chat.id, f'Я выбрал {bot_move}')

    if user_move == bot_move:
        bot.send_message(call.message.chat.id, 'Ничья')
    elif (user_move == 'Камень' and bot_move == 'Ножницы') or \
         (user_move == 'Ножницы' and bot_move == 'Бумага') or \
         (user_move == 'Бумага' and bot_move == 'Камень'):
        bot.send_message(call.message.chat.id, 'Ты победил')
    else:
        bot.send_message(call.message.chat.id, 'Я выиграл')

# Команда /start2 для случайных анекдотов
jokes = ['Почему программисты не любят природу? Слишком много багов.', 'Почему Java-программисты носят очки? Потому что они не могут C#.', 'Что сказал сервер на вечеринке? "Извините за лаг, я просто overloaded!']

@bot.message_handler(commands=['start2'])
def start2(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_quote = telebot.types.KeyboardButton('Случайный анекдот')
    keyboard.add(key_quote)
    bot.send_message(message.chat.id,
                     'Привет! Нажми на кнопку, чтобы получить случайный анекдот.',
                     reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Случайный анекдот')
def quote_message(message):
    send_joke(message)

def send_joke(message):
    quote = random.choice(jokes)
    bot.send_message(message.chat.id, quote)

bot.infinity_polling()
