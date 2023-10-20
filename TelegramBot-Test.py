import telebot 
from telebot import types

bot = telebot.TeleBot('6674584002:AAE_K3uIujOA8CBrKgNWd4Va5enq_bhUDTU')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Проверить погоду🌤️')
        btn2 = types.KeyboardButton('Коммунальные услуги🏠')
        btn3 = types.KeyboardButton('Список выполненной работы🪛')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓Самое время записать 😌 ', reply_markup=markup) #ответ бота


    elif message.text == 'Проверить погоду🌤️':
        bot.send_message(message.from_user.id, '*', parse_mode='Markdown')

    elif message.text == 'Коммунальные услуги🏠':
        bot.send_message(message.from_user.id, '*', parse_mode='Markdown')
    elif message.text == 'Список выполненной работы🪛':
        bot.send_message(message.from_user.id, '*', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть!