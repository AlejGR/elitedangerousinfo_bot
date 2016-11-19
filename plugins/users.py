#encoding=utf8
from config import *

@bot.message_handler(commands=['usuarios'])
def usuarioscontar(m):
    uid = m.from_user.id
    cid = m.chat.id
    archivo= open("usuarios.txt", "r")
    contenidousuario = archivo.read()
    lineas = len(open('usuarios.txt').readlines())
    if uid in administrador:
        bot.send_message(cid, contenidousuario + "\n" + 'Nº de usuarios: ' +  str(lineas))
    else:
        bot.send_message(cid, "Esta información es confidencial.")
