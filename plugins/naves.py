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
    item4 = types.KeyboardButton('Asp Scout')
    item5 = types.KeyboardButton('Beluga')
    item6 = types.KeyboardButton('Cañonera Federal')
    item7 = types.KeyboardButton('Clipper imperial')
    item8 = types.KeyboardButton('Cobra MkIII')
    item9 = types.KeyboardButton('Cobra MkIV')
    item10 = types.KeyboardButton('Correo Imperial')
    item11 = types.KeyboardButton('Diamondback Explorer')
    item12 = types.KeyboardButton('Diamondback Scout')
    item13 = types.KeyboardButton('Eagle')
    item14 = types.KeyboardButton('Eagle Imperial')
    item15 = types.KeyboardButton('F63 Condor')
    item16 = types.KeyboardButton('Fer-De-Lance')
    item17 = types.KeyboardButton('GU-97')
    item18 = types.KeyboardButton('Hauler')
    item19 = types.KeyboardButton('Keelback')
    item20 = types.KeyboardButton('Nave de Asalto Federal')
    item21 = types.KeyboardButton('Nave de Descenso Federal')
    item22 = types.KeyboardButton('Orca')
    item23 = types.KeyboardButton('Python')
    item24 = types.KeyboardButton('Sidewinder')
    item25 = types.KeyboardButton('Taipan')
    item26 = types.KeyboardButton('Type 6')
    item27 = types.KeyboardButton('Type 7')
    item28 = types.KeyboardButton('Type 9')
    item29 = types.KeyboardButton('Viper MkIII')
    item30 = types.KeyboardButton('Viper MkIV')
    item31 = types.KeyboardButton('Vulture')
    item32 = types.KeyboardButton('Inicio')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26, item27, item28, item29, item30, item31, item32)
    bot.send_message(m.chat.id, "Selecione una opción: ", reply_markup=markup)
    userStep[m.chat.first_name] = 'comandante'

@bot.message_handler(func=lambda m: get_user_step(m.chat.first_name) == 'comandante', content_types=['text'])
def stepnave(m):
    cid = m.chat.id
    msg = m.text[:20]
    msgmin = msg.lower()
    naves = ['adder', 'anaconda', 'asp explorer','asp scout','beluga','cañonera federal','clipper imperial','cobra mkiii','cobra mkiv','correo imperial','diamondback explorer','diamondback scout','eagle mkii','f63 condor','fer-de-lance','gu-97','hauler','imperial eagle','keelback','nave de asalto federal','nave de descenso federal', 'orca', 'python','sidewinder','taipan','type 6', 'type 7', 'type 9', 'viper mkiii', 'viper mkiv', 'vulture']
    if msgmin == "inicio":
        userStep[m.from_user.first_name] = 0
    else:
        if msgmin in naves:
                #archivo = open("extras/naves/" + str(msgmin) + ".txt", "r")
                nave = archivo.read()
                bot.send_photo(cid,open("extras/nuevas_naves" + str(msgmin) + '.png','rb'))
                bot.send_message(cid,nave, parse_mode="Markdown", disable_web_page_preview="True")
        else:
                bot.send_message(cid, "Esa nave no existe o aún no está en nuestra base de datos.")
    bot.send_message(administrador, "[AVISO - INFO] Nave usado por " + str(m.from_user.first_name))
