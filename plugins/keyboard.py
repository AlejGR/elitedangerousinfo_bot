#encoding=utf8

from config import *

@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in ['Inicio'])

@bot.message_handler(commands=['inicio'])
def command_info(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Sistemas')
    item2 = types.KeyboardButton('Productos')
    item3 = types.KeyboardButton('Radios')
    item4 = types.KeyboardButton('Ayuda')
    item5 = types.KeyboardButton('Creditos')
    item6 = types.KeyboardButton('Contactar')
    item7 = types.KeyboardButton('Nave')
    item8 = types.KeyboardButton('Ocultar Teclado')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    userStep[m.from_user.first_name] = 0
    bot.send_message(m.chat.id, "Selecione una opción: ", reply_markup=markup)

@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in ["Ocultar Teclado"])

@bot.message_handler(commands=['ocultarteclado'])
def command_hideboard(m):
    cid = m.chat.id
    bot.send_message(cid,"Ocultando teclado",reply_markup=types.ReplyKeyboardHide())

    #bot.send_message(m.chat.id,"Prueba")
    #markup = types.InlineKeyboardMarkup()
    #b1 = types.InlineKeyboardButton("Sistemas")
    #b2 = types.InlineKeyboardButton("Productos")
    #b3 = types.InlineKeyboardButton("Radios")
    #b4 = types.InlineKeyboardButton("Ayuda")
    #b5 = types.InlineKeyboardButton("Contactar")
    #b6 = types.InlineKeyboardButton("Nave")
    #markup.add(b1, b2, b3, b4, b5, b6)
