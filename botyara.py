import telebot
from telebot import types

bot = telebot.TeleBot("7695889185:AAFrf9U7XrZkagx1lmfRxcd0IrXB2JqsLwI")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "мне самому нужна помощь")


@bot.message_handler(commands=['author'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text ='мой вк', url ='https://vk.com/s.galustyan2014')
    markup.add(btn1)
    bot.send_message(message.chat.id, 'снизу ссылка на мою страничку ВК', reply_markup=markup)

@bot.message_handler(commands = ['switch'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='выбирай, собсна', switch_inline_query="Telegram")
    markup.add(switch_button)
    bot.send_message(message.chat.id, "Выбрать чат", reply_markup = markup)

bot.infinity_polling()

