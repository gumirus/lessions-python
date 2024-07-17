import telebot

token = '6835062044:AAFsRbl5CGo-NsgblLrLQpCQMCcH8G0bsIE'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    """
    Обрабатывает текстовые сообщения от пользователя.
    Делит сообщение на строки, проверяет их количество
    и создает опрос, если количество строк корректное.
    """
    lst = message.text.split('\n')
    
    if len(lst) < 3:
        bot.reply_to(message, "Сообщение должно содержать не менее 3 строк.")
    elif len(lst) > 11:
        bot.reply_to(message, "Сообщение должно содержать не более 11 строк.")
    else:
        question = lst[0]
        options = lst[1:]
        
        bot.send_poll(
            chat_id=message.chat.id,
            question=question,
            options=options,
            is_anonymous=True
        )

if __name__ == '__main__':
    bot.infinity_polling()
