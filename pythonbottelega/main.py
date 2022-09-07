import telebot
import constants as v
bot = telebot.TeleBot(v.API_KEY, parse_mode=None)
print("бот ебашит")
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, v.helloMsg)
# @bot.message_handler(commands=['help'])
# def send_help(message):
# 	bot.reply_to(message, "If u need help do this: ")

@bot.message_handler(func=lambda message: True)
def handle_stuff(message):
    # кидать текст
    if message.text.lower() == "чайковский":
        bot.reply_to(message, v.text2)
    elif message.text.lower() in ["imall", "аймол"]:
        bot.reply_to(message, v.text1)
    elif message.text.lower() == "картина":
        bot.reply_to(message, v.text4)
    elif message.text.lower() == "улица":
        bot.reply_to(message, v.text5)
    elif message.text.lower() == "книга":
        bot.reply_to(message, v.text3)
    elif message.text.lower() == "зож":
        bot.reply_to(message, v.text6)
    elif message.text.lower() == "карусель":
        bot.reply_to(message, v.text7)
    elif message.text.lower() == "саша":
        bot.reply_to(message, v.text8)
    elif message.text.lower() == "миша":
        bot.reply_to(message, v.text9)
    elif message.text.lower() == "сахар":
        bot.reply_to(message, v.text10)
    # prekoli
    # elif message.text.lower() == "да":
    #     bot.reply_to(message, "пизда")
    # elif message.text.lower() in ["пед", "пггпу"]:
    #     bot.reply_to(message, "самый лучший университет мира!")
    elif message.text.lower() == "соль":
        bot.reply_to(message, "мы таким здесь не занимаемся")
    # elif message.text.lower() == "привет":
    #     bot.reply_to(message, "пока")
    # elif message.text.lower() == "хуй":
    #     bot.reply_to(message, "тебе")

    # кидать картинки
    # elif message.text.lower() == "send boobs":
    #     img = open("images/tits.jpg", "rb")
    #     bot.send_photo(message.chat.id, photo=img)
    #     img.close()


    else:
        bot.reply_to(message, "Код неверный")


bot.infinity_polling()