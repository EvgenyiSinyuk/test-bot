import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Привет, Марк!"),
               types.KeyboardButton("Как дела?)"),
               types.KeyboardButton("Все остальные кнопки тестовые."))
    markup.add(types.KeyboardButton("Пустая тестовая кнопка👋"),
               types.KeyboardButton("Пустая тестовая кнопка👋"),
               types.KeyboardButton("Пустая тестовая кнопка👋"))
    markup.add(types.KeyboardButton("Пустая тестовая кнопка👋"),
               types.KeyboardButton("Пустая тестовая кнопка👋"),
               types.KeyboardButton("Пустая тестовая кнопка👋"))

    bot.send_message(message.chat.id, 'Привет! Ты активировал тестового бота для Марка', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    try:
        if message.text == 'Привет, Марк!':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Привет!", callback_data="well"))
            markup.add(types.InlineKeyboardButton("Отвали!", callback_data="bad"))
            bot.send_message(chat_id=message.chat.id, text="Hi, Mark!", reply_markup=markup)

        elif message.text == 'Пустая тестовая кнопка👋':
            bot.send_message(chat_id=message.chat.id, text="Это просто тестовая кнопка")

        elif message.text == 'Все остальные кнопки тестовые.':
            bot.send_message(chat_id=message.chat.id, text="Это просто тестовая кнопка")
            
        elif message.text == 'Как дела?)':
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Хорошо", callback_data="well"))
            markup.add(types.InlineKeyboardButton("Плохо", callback_data="bad"))
            bot.send_photo(message.chat.id, 'https://rubberslug.s3.amazonaws.com/user/4/8ffbda03c8e4fcf97b22c43b63107f8/vbzgst95bd_o.jpg')
            bot.send_message(chat_id=message.chat.id, text="Ну как дела?!", reply_markup=markup)

    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'well':
                bot.send_message(chat_id=call.message.chat.id, text="Будь здоров!")

            elif call.data == 'bad':
                bot.send_message(chat_id=call.message.chat.id, text="Ну что ты так(")
    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
