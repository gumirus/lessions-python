# import telebot

# token = ""

# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['photo'])
# def send_photo(message):
#   bot.send_photo(message.chat.id,"https://kartin.papik.pro/uploads/posts/2023-06/1686890149_kartin-papik-pro-p-kartinki-dlya-statusa-vatsap-tsveti-42.jpg")

# @bot.message_handler(commands=['local_photo'])
# def local(message):
#   bot.send_photo(message.chat.id, 
#                  open ('1-png', 'rb'))

# @bot.message_handler(commands=['music'])
# def send_music(message):
#   bot.send_audio(message.chat.id,
#                 open ('Study and Relax.mp3' ,'rb'),
#                 caption='For study',
#                 title='Study and Relax')
# @bot.message_handler(content_types=['doc'])
# def send_doc (message):
#   bot.send_document(message.chat.id,
#                     open ('1.pdf', 'rb'))
  
# from gtts import gTTS

# @bot.message_handler(content_types=['text'])
# def text_to_speech(message) :
#   tts = gTTS(message.text, lang='ru')
#   tts.save('audio.ogg')
#   bot.send_voice(message.chat.id,
#                open ('audio.ogg', 'rb'))

# @bot.message_handler (commands=[' set_media' ])
# def send_set_media(message):
#   medias = [
#     telebot.types.InputMediaPhoto("")
#     telebot.types.InputMediaPhoto("")
#     telebot.types.InputMediaPhoto("")
#     telebot.types.InputMediaPhoto("")
#   ]
#   bot. send_media_group (message.chat.id, medias)

# @bot.message_handler (commands=['venue'])
# def send_ven (message) :
#   bot.send_venue(message.chat.id, 75, 58, 'Остров Северный', 'Архангельская область')

# @bot.message_handler(commands=['contact'])
# def send_con(message):
#   bot.send_contact (message.chat.id,'+79999999', 'Ruslan')

# @bot.message_handler(commands=['poll'])
# def poll(message):
#   que = 'Как дела?'
#   ans = ['Нормальное', "Хорошо", "Лучше чем у тех двух"]

#   bot. send_poll(message.chat.id, que, ans)

# @bot.message_handler(commands=['dice'])
# def dice(message):
#   bot.send_dice(message.chat.id)

# @bot.message_handler(content_types=['sticker'])
# def send_sticker(message) :
#   bot.send_sticker(message.chat.id,
#                    message.sticker.file_id)


# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
# from pymorphy2 import MorphAnalyzer
# nltk.download('stopwords')
# nltk.download('punkt')

# morph = MorphAnalyzer()
# stopWords = set(stopwords.words('russian'))

# def get_summary (text):
#   words = word_tokenize(text)
#   freqTable = dict()
#   for word in words:
#       word = morph.parse(word. lower())[0].normal_form
#       if word in stopWords:
#          freqTable[word] += 1
#       else:
#           freqTable[word] = 1

#   sentences = sent_tokenize(text)
#   sentenceValue = dict()
#   for sentence in sentences:
#     for word in word_tokenize(sentence) :
#         word = morph. parse(word.lower())[0].normal_form
#         if word in freqTable:
#            if sentence in sentenceValue:
#               sentenceValue[sentence] += freqTable[word]
#            else:
#               sentenceValue[sentence] = freqTable[word]
#   sumValues = sum(sentenceValue.values())
#   averge = int(sumValues / len(sentenceValue))
#   maxValue = max(sentenceValue.values())
#   summary = ''
#   for sentence in sentences:
#       if ((sentence in sentenceValue) and
#       ((1.2 * averge) < sentenceValue[sentence] < (0.8 * maxValie))): 
#         summary += " " + sentence


# bot.infinity_polling()


import telebot
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from pymorphy2 import MorphAnalyzer
import os

# Токен вашего бота
token = ""
bot = telebot.TeleBot(token)

# Инициализация морфологического анализатора и загрузка стоп-слов
morph = MorphAnalyzer()
nltk.download('stopwords')
nltk.download('punkt')
stopWords = set(stopwords.words("russian"))

# Функция для создания краткого содержания текста
def get_summary(text):
    words = word_tokenize(text)
    freqTable = dict()
    for word in words:
        word = morph.parse(word.lower())[0].normal_form
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()
    for sentence in sentences:
        for word in word_tokenize(sentence):
            word = morph.parse(word.lower())[0].normal_form
            if word in freqTable:
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freqTable[word]
                else:
                    sentenceValue[sentence] = freqTable[word]

    sumValues = sum(sentenceValue.values())
    average = int(sumValues / len(sentenceValue))
    maxValue = max(sentenceValue.values())

    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and ((1.2 * average) < sentenceValue[sentence]):
            summary += " " + sentence
    return summary

# Обработчик сообщений с типом 'document'
@bot.message_handler(content_types=['document'])
def send_text(message):
    # Получаем информацию о файле по его id
    info = bot.get_file(message.document.file_id)
    # Получаем путь к файлу
    path = info.file_path
    # Загружаем (скачиваем) файл
    file = bot.download_file(path)
    
    # Создаём директорию для сохранения файлов, если её нет
    media_dir = '/Users/agori/OneDrive/Рабочий стол/tbgot/media'
    if not os.path.exists(media_dir):
        os.makedirs(media_dir)
    
    # Полный путь для сохранения файла
    file_path = os.path.join(media_dir, os.path.basename(path))
    
    # Сохраняем скачанный файл
    with open(file_path, 'wb') as f:
        f.write(file)
    
    # Читаем содержимое файла и создаём его краткое содержание
    with open(file_path, 'r', encoding='utf-8') as f:
        summary = get_summary(f.read())
    
    # Записываем краткое содержание обратно в файл
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    # Отправляем обработанный файл обратно пользователю
    bot.send_document(message.chat.id, open(file_path, 'rb'))

if __name__ == '__main__':
    bot.infinity_polling()
