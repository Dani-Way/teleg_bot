import telebot
import config
 
from telebot import types
 
bot = telebot.TeleBot(config.token)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заявки")
    item2 = types.KeyboardButton("Что-то ещё")
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Приветсвую вас, тут вы можете проверять заявки с сайта!", reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    peer_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'Заявки':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Принять", callback_data='good')
            item2 = types.InlineKeyboardButton("Отклонить", callback_data='bad')
            markup.add(item1, item2)
            bot.send_message(peer_id, "Новая заявка", reply_markup=markup)
            
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Заявки")
            item2 = types.KeyboardButton("Что-то ещё")
            markup.add(item1, item2)
         
            bot.send_message(message.chat.id, "Вы перешли в главное меню!", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    peer_id = call.message.chat.id
    try:
        if call.message:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Назад")
            markup.add(item1)
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Данная заявка принята', reply_markup=markup)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новая заявка", reply_markup=None)
            elif call.data == 'bad':
                bot.send_message(peer_id, 'Данная заявка отклонена', reply_markup=markup)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новая заявка", reply_markup=None)
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)