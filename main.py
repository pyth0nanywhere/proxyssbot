import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '6970331121:AAH_ns6WX_rwrXglWeYPWPRubDwFkHExoyM'
bot = telebot.TeleBot(TOKEN)


# Обробник команди '/start'
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    test_button = KeyboardButton("Посмотреть количество прокси для Франции")
    markup.add(test_button)
    bot.send_message(message.chat.id,  'Выберите опцию', reply_markup=markup)

# Обробник команди '/parsing'
@bot.message_handler(func=lambda message: message.text == "Посмотреть количество прокси для Франции")
def parsing(message):

    # Замість простого requests.get, використовуйте такий виклик з налаштуваннями проксі
    url = 'https://proxy6.net/api/564ab318ff-34ffe93bad-6d84224847/getcount?country=fr&version=4'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        count_proxy = data['count']
        bot.send_message(message.chat.id, f'Кол-во доступных прокси для Франции: {count_proxy}')
    else:
        bot.send_message(message.chat.id, f'Ошибка при запросе, попробуй позже: {response.status_code}')

bot.polling(none_stop=True)
