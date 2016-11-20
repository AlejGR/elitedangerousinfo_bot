#encoding=utf8
from config import *


@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in ['Nave'])

@bot.message_handler(commands=['nave'])
def command_naves(m):
    cid = m.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Adder')
    item2 = types.KeyboardButton('Anaconda')
    item3 = types.KeyboardButton('Asp Explorer')
    item4 = types.KeyboardButton('Cobra MkIII')
    item5 = types.KeyboardButton('Diamondback Explorer')
    item6 = types.KeyboardButton('Diamondback Scout')
    item7 = types.KeyboardButton('Eagle')
    item8 = types.KeyboardButton('Fer-De-Lance')
    item9 = types.KeyboardButton('Hauler')
    item10 = types.KeyboardButton('Orca')
    item11 = types.KeyboardButton('Python')
    item12 = types.KeyboardButton('Sidewinder')
    item13 = types.KeyboardButton('Type 6')
    item14 = types.KeyboardButton('Type 7')
    item15 = types.KeyboardButton('Type 9')
    item16 = types.KeyboardButton('Viper MkIII')
    item17 = types.KeyboardButton('Vulture')
    item18 = types.KeyboardButton('Inicio')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18)
    bot.send_message(m.chat.id, "Selecione una opción: ", reply_markup=markup)
    userStep[m.chat.first_name] = 'comandante'

@bot.message_handler(func=lambda m: get_user_step(m.chat.first_name) == 'comandante', content_types=['text'])
def stepnave(m):
    cid = m.chat.id
    msg = m.text[:20]
    msgmin = msg.lower()
    naves = ['adder', 'anaconda', 'asp explorer','cobra mkiii', 'diamondback explorer', 'diamondback scout', 'eagle', 'fer-de-lance', 'hauler', 'orca', 'python', 'sidewinder', 'type 6', 'type 7', 'type 9', 'viper mkiii', 'vulture']
    if msgmin == "inicio":
        userStep[m.from_user.first_name] = 0
    else:
        if msgmin in naves:
                archivo = open("extras/naves/" + str(msgmin) + ".txt", "r")
                nave = archivo.read()
                bot.send_photo(cid,open("extras/naves/" + str(msgmin) + '.jpg','rb'))
                bot.send_message(cid,nave, parse_mode="Markdown", disable_web_page_preview="True")
        else:
                bot.send_message(cid, "Esa nave no existe o aún no está en nuestra base de datos.")
