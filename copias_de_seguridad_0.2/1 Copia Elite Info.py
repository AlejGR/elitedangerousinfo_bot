 #encoding=utf8
import telebot
from telebot import types
import time
import sys
from imp import reload
import urllib3
reload(sys)
import requests
import json
import pymongo
from pymongo import MongoClient


administrador = [11186174]
TOKEN = '180904359:AAEB0HUi2dkuM-IfIis7beISFWTmOTuiEl8'
usuarios = [line.rstrip('\n') for line in open('usuarios.txt')] # Cargamos la lista de usuarios.
numeros = [line.rstrip('\n') for line in open('numeros.txt')] # Cargamos la lista de usuarios.
bot = telebot.TeleBot ('180904359:AAEB0HUi2dkuM-IfIis7beISFWTmOTuiEl8')


def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            if cid > 0:
                mensaje = str(m.chat.first_name) + " [" + str(cid) + " - " + time.strftime("%c") + "]: " + m.text
            else:
                mensaje = str(m.from_user.first_name) + "[" + str(m.chat.title) + " - " + time.strftime("%c") + "]: " + m.text
            f = open('log.txt', 'a')
            f.write(mensaje + "\n")
            f.close()
            print (mensaje)

bot.set_update_listener(listener)

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
            bot.send_message(11186174,"Nuevo Usuario" + "\n" + "Usuario: " + str(name) + " - " + str(m.chat.username) + "\n" + "ID: " + str(cid))
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
  
#################################
#        COMANDOS AYUDA         #
#################################

@bot.message_handler(commands=['ayuda'])
def ayuda(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece Información de Elite Dangerous, los comandos disponibles son: \n /sistemas <Nombre del sistemas> (La búsqueda distingue entre mayúsculas y minúsculas \n \n *Versión: 0.1 Beta*", parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))    
        else:
            pass
    else:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece Información de Elite Dangerous, los comandos disponibles son: \n /sistemas <Nombre del sistemas> (La búsqueda distingue entre mayúsculas y minúsculas \n \n *Versión: 0.1 Beta*", parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))
        else:
            pass
        
@bot.message_handler(commands=['help'])
def help(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece Información de Elite Dangerous, los comandos disponibles son: \n /sistemas <Nombre del sistemas> (La búsqueda distingue entre mayúsculas y minúsculas \n \n *Versión: 0.1 Beta*", parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))    
        else:
            pass
    else:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece Información de Elite Dangerous, los comandos disponibles son: \n /sistemas <Nombre del sistemas> (La búsqueda distingue entre mayúsculas y minúsculas \n \n *Versión: 0.1 Beta*", parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))
        else:
            pass
        
@bot.message_handler(commands=['contactar'])
def command_contactar(m):
    cid = m.chat.id
    name =m.chat.first_name
    msg = m.text[10:]
    #res = bot.reply_to(msg, "Escriba a continuación el mensaje.")
    #bot.register_next_step_handler(res, contacto_handler)
    if m.text[10:] != '':
        bot.send_message( cid, "Mensaje <" + m.text[10:] + " > enviado con éxito.")
        bot.send_message( 11186174, "*Mensaje*:" + msg  + "\n" + "*Usuario*: " + str(name) + " - " + "@" + str(m.from_user.username) + "\n" + "*ID*: " + str(cid), parse_mode="Markdown")
    else:
         bot.send_message( cid, "Error, Tienes que poner '/contactar cualquier mensaje'. Ejemplo:\n/contactar Hola.")
    
#################################
#   ACCESO A LA BASE DE DATOS   #
#################################
client = MongoClient('localhost:27017')
db = client.elitedangerous # o ed
with open('systems.json') as f:
    systems = json.load(f)

@bot.message_handler(commands=['sistemas'])
def command_sistemas(m):
    cid = m.chat.id
    if len(m.text.split()) >= 2:
        name = m.text.split(' ',1)[1]
        a = db.sistemas.find_one({'name': name})
        if a:
            consulta = "*Nombre del Sistema*: {}\n*Potencia*: {}\n*Estado*: {}\n*Aliado*: {}\n*Facción*: {}\n*Gobierno*: {}\n*Economía Primaria*: {}\n*Población*: {}\n*Coordenadas*:\n \t *X*: {} \n \t *Y*: {} \n \t *Z*: {} ".format(
            a.get('name'),
            a.get('power'),
            a.get('state'),
            a.get('allegiance'),
            a.get('faction'),
            a.get('government'),
            a.get('primary_economy'),
            a.get('population'),
            a.get('x'),
            a.get('y'),
            a.get('z')
            )
        else:
            consulta = "Me da que eso no existe."
    else:
        consulta = "Macho, pon el nombre"
    
    bot.send_message(cid, consulta, parse_mode="Markdown")

bot.polling(none_stop=True)