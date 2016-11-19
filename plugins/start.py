#encoding=utf8
from config import *

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    name = m.chat.first_name
    if cid > 0:
        if not str(cid) in numeros: # Con esta sentencia, hacemos que solo se ejecute lo de abajo cuando un usuario hace uso del bot por primera vez.
            usuarios.append(str(cid)) # En caso de no estar en la lista de usuarios, lo añadimos.
            aux = open('usuarios.txt', 'a') # Y lo insertamos en el fichero 'usuarios.txt'
            aux.write( str(name) + "\n")
            aux.close()
            numeros.append(str(cid))
            aux = open('numeros.txt', 'a') # Y lo insertamos en el fichero 'usuarios.txt'
            aux.write( str(cid) + "\n")
            aux.close()
            bot.send_message( cid, "Bienvenido, comandante "+ str(m.chat.first_name) + " o7")
            bot.send_message(administrador,"Nuevo Usuario" + "\n" + "Usuario: " + str(name) + " - " + "@"  + str(m.chat.username) + "\n" + "ID: " + str(cid))
        else:
             if not str(cid) in numeros:
                usuarios.append(str(cid)) # En caso de no estar en la lista de usuarios, lo añadimos.
                aux = open('numeros.txt', 'a') # Y lo insertamos en el fichero 'usuarios.txt'
                aux.write( str(cid) + "\n")
                aux.close()
                usuarios.append(str(cid)) # En caso de no estar en la lista de usuarios, lo añadimos.
                aux = open('usuarios.txt', 'a') # Y lo insertamos en el fichero 'usuarios.txt'
                aux.write( str(m.chat.title) + "\n")
                aux.close()
                bot.send_message( cid ,"Hola,soy el bot destinado a Elite: Dangerous, encantado de estar en "+ str(m.chat.title))
