import telebot
import TOKEN
import random
 
from telebot import types
 
bot = telebot.TeleBot(TOKEN.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    print('REGISTR_USER | ', message.chat.id, " |  {0.first_name}".format(message.from_user, bot.get_me()))
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Камень🗿")
    item2 = types.KeyboardButton("Ножницы✂️")
    item3 = types.KeyboardButton("Бумага🧻")
 
    markup.add(item1, item2, item3)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>🗿✂️🧻, бот созданный чтобы сыграть с вами в всем известную игру Камень Ножницы Бумага :).".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Камень🗿':
        	rad = random.randint(0,2)
        	if rad == 0:
        		bot.send_message(message.chat.id,'Камень🗿')
        		bot.send_message(message.chat.id,'Ничья')

        	if rad == 1:
        		bot.send_message(message.chat.id,'Ножницы✂️')
        		bot.send_message(message.chat.id,'Я проиграл😞')

        	if rad == 2:
        		bot.send_message(message.chat.id,'Бумага🧻')
        		bot.send_message(message.chat.id,'Я выйграл!😃')
        	
        if message.text == 'Ножницы✂️':
        	rad = random.randint(0,2)
        	if rad == 0:
        		bot.send_message(message.chat.id,'Камень🗿')
        		bot.send_message(message.chat.id,'Я выйграл!😃')

        	if rad == 1:
        		bot.send_message(message.chat.id,'Ножницы✂️')
        		bot.send_message(message.chat.id,'Ничья')

        	if rad == 2:
        		bot.send_message(message.chat.id,'Бумага🧻')
        		bot.send_message(message.chat.id,'Я проиграл😞')
        if message.text == 'Бумага🧻':
        	rad = random.randint(0,2)
        	if rad == 0:
        		bot.send_message(message.chat.id,'Камень🗿')
        		bot.send_message(message.chat.id,'Я проиграл😞')

        	if rad == 1:
        		bot.send_message(message.chat.id,'Ножницы✂️')
        		bot.send_message(message.chat.id,'Я выйграл!😃')

        	if rad == 2:
        		bot.send_message(message.chat.id,'Бумага🧻')
        		bot.send_message(message.chat.id,'Ничья')

           

# RUN
bot.polling(none_stop=True)