#encoding=utf8
from config import *

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    name = m.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Sistemas')
    item2 = types.KeyboardButton('Productos')
    item3 = types.KeyboardButton('Radios')
    item4 = types.KeyboardButton('Ayuda')
    item5 = types.KeyboardButton('Creditos')
    item6 = types.KeyboardButton('Informacion')
    item7 = types.KeyboardButton('Contactar')
    item8 = types.KeyboardButton('Nave')
    item9 = types.KeyboardButton('Ocultar Teclado')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
    if cid > 0:
        if not str(cid) in numeros: # Con esta sentencia, hacemos que solo se ejecute lo de abajo cuando un usuario hace uso del bot por primera vez.
            usuarios.append(str(cid)) # En caso de no estar en la lista de usuarios, lo añadimos.
            aux = open('extras/usuarios.txt', 'a') # Y lo insertamos en el fichero 'usuarios.txt'
            aux.write( str(name) + "\n")
            aux.close()
            numeros.append(str(cid))
            aux = open('extras/numeros.txt', 'a') # Y lo insertamos en el fichero 'usuarios.txt'
            aux.write( str(cid) + "\n")
            aux.close()
            bot.send_message( cid, "Bienvenido, comandante "+ str(m.chat.first_name) + " o7", reply_markup=markup)
            bot.send_message(administrador,"Nuevo Usuario" + "\n" + "Usuario: " + str(name) + " - " + "@"  + str(m.chat.username) + "\n" + "ID: " + str(cid))
        else:
             if not str(cid) in numeros:
                usuarios.append(str(cid)) # En caso de no estar en la lista de usuarios, lo añadimos.
                aux = open('extras/numeros.txt', 'a') # Y lo insertamos en el fichero 'usuarios.txt'
                aux.write( str(cid) + "\n")
                aux.close()
                usuarios.append(str(cid)) # En caso de no estar en la lista de usuarios, lo añadimos.
                aux = open('extras/usuarios.txt', 'a') # Y lo insertamos en el fichero 'usuarios.txt'
                aux.write( str(m.chat.title) + "\n")
                aux.close()
                bot.send_message( cid ,"Hola,soy el bot destinado a Elite: Dangerous, encantado de estar en "+ str(m.chat.title))
