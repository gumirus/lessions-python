import telebot

# бот и токен
bot = telebot.TeleBot('токен от телеграм ботОтец')

# функция для сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    #  сообщения от телеграмм
    user_message = message.text
    
    # дублирование
    response_message = (user_message + ' ') * 10
    
    # обратное сообщение в телеграмм
    bot.send_message(message.chat.id, response_message)

# запуск бота
bot.polling()

if __name__ == '__main__':
    bot.polling(none_stop=True)
