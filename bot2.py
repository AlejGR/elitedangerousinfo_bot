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


administrador = [11186174, 158789972, 4891212, 37690722]
Pi = 158789972
TOKEN = '225774062:AAGtKh6YkQa8Q-OOC1jf_fpLvDo4jvgNOaw'
usuarios = [line.rstrip('\n') for line in open('usuarios.txt')] # Cargamos la lista de usuarios.
numeros = [line.rstrip('\n') for line in open('numeros.txt')] # Cargamos la lista de usuarios.
bot = telebot.TeleBot ('225774062:AAGtKh6YkQa8Q-OOC1jf_fpLvDo4jvgNOaw')
userStep=dict()

def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            if cid > 0:
                mensaje = str(m.chat.first_name) + " [" + str(cid) + " - " + time.strftime("%c") + "]: " + m.text
            else:
                mensaje = str(m.from_user.first_name) + "-" + str(m.from_user.id) + "[" + str(m.chat.title) +str(cid) + " - " + time.strftime("%c") + "]: " + m.text
            f = open('log.txt', 'a')
            f.write(mensaje + "\n")
            f.close()
            print (mensaje)

bot.set_update_listener(listener)

############################################
#                DEFINICIONES              #
############################################
def command_galnetprivado(m):
    cid = m.chat.id
    archivo = open("galnet.txt", "r") 
    contenido = archivo.read()
    if cid > 0:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, contenido)
        bot.send_message(11186174, "[AVISO] Galnet usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")" + " Através de enlace de grupo")

def command_cgprivado(m):
    cid = m.chat.id
    archivo = open("cg.txt", "r")
    contenido = archivo.read()
    if cid > 0:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, contenido)
        bot.send_message(11186174, "[AVISO] Community Goal usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")" + " Através de enlace de grupo")
        

############################################
#                 COMANDOS                 #
############################################        

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
            bot.send_message( cid, "Bienvenido al bot del Galnet en español comandante "+ str(m.chat.first_name) + " o7")
            bot.send_message(11186174,"Nuevo Usuario" + "\n" + "Usuario: " + str(name) + " - " + "@" + str(m.from_user.username) + "\n" + "ID: " + str(cid))
        else:
            bot.send_message( cid, "Comandate "+ str(m.chat.first_name) + " usted está ya en nuestra base de datos.")
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
            bot.send_message( cid ,"Hola,soy el bot destinado al Galnet en Español, encantado de estar en "+ str(m.chat.title))
         else:
            bot.send_message( cid ,"El grupo "+ str(m.chat.title) + " está ya registrado en nuestra base de datos.")
    comando = m.text[7:]
    if comando == 'galnet':
        command_galnetprivado(m)
    elif comando == 'cg':
        command_cgprivado(m)
            
#########
# AYUDA #
#########   
            
@bot.message_handler(commands=['ayuda'])
def ayuda(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece noticias de Elite Dangerous, los comandos disponibles son: \n \n *Galnet* \n /publicar \n /galnet \n /subirgalnet \n /publicargalnet \n /modificargalnet \n /descargargalnet \n \n *CG* \n /cg \n /subircg \n /subircg1 \n /subircg2 \n \subircg3 \n /publicarcg \n /modificarcg \n /descargarcg", parse_mode="Markdown")
        else:
            pass
    else:
        if cid > 0 :
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece noticias de Elite Dangerous, los comandos disponibles son: \n \n *Galnet* \n /galnet \n \n *CG* \n /cg", parse_mode="Markdown")
        else:
            pass
        
@bot.message_handler(commands=['help'])
def help(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece noticias de Elite Dangerous, los comandos disponibles son: \n \n *Galnet* \n /publicar \n /galnet \n /subirgalnet \n /publicargalnet \n /modificargalnet \n /descargargalnet \n \n *CG* \n /cg \n /subircg \n /subircg1 \n /subircg2 \n /subircg3 \n /publicarcg \n /modificarcg \n /descargarcg", parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO] Ayuda usado por " + str(m.from_user.first_name))    
        else:
            pass
    else:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece noticias de Elite Dangerous, los comandos disponibles son: \n \n *Galnet* \n /galnet \n \n *CG* \n /cg", parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO] Ayuda usado por " + str(m.from_user.first_name))
        else:
            pass
        
############
# PUBLICAR #
############  
@bot.message_handler(commands=['publicar'])
def publicardirecto(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame Texto a publicar')
        userStep[m.from_user.first_name] = 'comandantepublicardirecto'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")

@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandantepublicardirecto', content_types=['text'])
def publicardirecto2(m):
    cid = m.chat.id
    msg = m.text
    with open('publicar.txt', 'wb') as docu:
        docu.write(msg.encode('utf-8'))
    userStep[m.from_user.first_name] = 0
    archivo = open("publicar.txt", "r") 
    contenido = archivo.read()
    bot.send_message(m.chat.id,'El texto se publicará en breve.')
    bot.send_message("@EliteDangerousESP", contenido, parse_mode="Markdown")

            
  ####################            
  #      GALNET      #
  ####################
  
def get_user_step(usuariogalnet):
    if usuariogalnet in userStep:
        return userStep[usuariogalnet]
    return 0

@bot.message_handler(commands=['subirgalnet'])
def subirgalnet(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame el texto del Galnet con Markdown')
        userStep[m.from_user.first_name] = 'comandante'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")

@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandante', content_types=['text'])
def archivogalnet(m):
    cid = m.chat.id
    msg = m.text
    with open('galnet.txt', 'wb') as docu:
        docu.write(msg.encode('utf-8') )
    bot.send_message(m.chat.id,'Galnet Actualizado.')
    userStep[m.from_user.first_name] = 0
    
@bot.message_handler(commands=['galnet'])
def galnet(m):
    cid = m.chat.id
    namsel = -36989419
    archivo = open("galnet.txt", "r") 
    contenido = archivo.read()
    if cid > 0:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Galnet usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        #bot.send_sticker(cid,open("tocho.webp", 'rb'))
    else:
        if cid == namsel:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, contenido, parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO] Galnet usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        else:
            bot.send_message(cid,"Pulsa aquí para ver la Última Noticia -->[Galnet](https://telegram.me/GalnetESP_BOT?start=galnet)", parse_mode="Markdown", reply_to_message_id=int(m.message_id), disable_web_page_preview = True)
    
@bot.message_handler(commands=['publicargalnet'])
def publicargalnet(m):
    archivo = open("galnet.txt", 'r')
    contenido = archivo.read()
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        msg = bot.send_message("@EliteDangerousESP", contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Galnet publicado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        bot.send_message(11186174,"Galnet publicado con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c"))
        bot.send_message(158789972,"Galnet publicado con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c"))
        bot.send_message(4891212,"Galnet publicado con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c"))
        
@bot.message_handler(commands=['modificargalnet'])
def modificargalnet(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not uid in administrador or len(m.text.split()) != 2:
        return
    msg_id = m.text.split()[1]
    msg_text = open('galnet.txt','r').read()
    try:
        bot.edit_message_text(msg_text, "@EliteDangerousESP", msg_id, parse_mode="Markdown")
        bot.send_message(cid, 'Galnet modificado')
    except Exception as e:
        bot.send_message(cid, e)

@bot.message_handler(commands=['descargargalnet'])
def descargargalnet(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_document(cid, open("galnet.txt", 'rb'))
        bot.send_message(11186174, "[AVISO] Galnet descargado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
            
  #################################            
  #        COMMUNITY GOALS        #
  #################################

@bot.message_handler(commands=['subircg'])
def subircg(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame el texto del Community Goal (el índice) con Markdown ')
        userStep[m.from_user.first_name] = 'comandantecg'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")

@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandantecg', content_types=['text'])
def archivocg(m):
    cid = m.chat.id
    msg = m.text
    with open('cg.txt', 'wb') as docu:
        docu.write(msg.encode('utf-8') )
    bot.send_message(m.chat.id,'Community Goal Actualizado.')
    userStep[m.from_user.first_name] = 0
 #################################            
 #        COMMUNITY GOALS 1      #
 #################################
@bot.message_handler(commands=['subircg1'])
def subircg1(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame el texto del Community Goal 1 con Markdown')
        userStep[m.from_user.first_name] = 'comandantecg1'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")

@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandantecg1', content_types=['text'])
def archivocg1(m):
    cid = m.chat.id
    msg = m.text
    with open('cg1.txt', 'wb') as docu:
        docu.write(msg.encode('utf-8') )
    bot.send_message(m.chat.id,'Community Goal 1 Actualizado.')
    bot.send_message(11186174, "[AVISO] Community Goal 1 Actualizado " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
    userStep[m.from_user.first_name] = 0

 #################################            
 #        COMMUNITY GOALS 2      #
 #################################
@bot.message_handler(commands=['subircg2'])
def subircg2(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame el texto del Community Goal 2 con Markdown')
        userStep[m.from_user.first_name] = 'comandantecg2'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")

@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandantecg2', content_types=['text'])
def archivocg2(m):
    cid = m.chat.id
    msg = m.text
    with open('cg2.txt', 'wb') as docu:
        docu.write(msg.encode('utf-8') )
    bot.send_message(m.chat.id,'Community Goal 2 Actualizado.')
    bot.send_message(11186174, "[AVISO] Community Goal 2 Actualizado " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
    userStep[m.from_user.first_name] = 0
    pass
 #################################            
 #        COMMUNITY GOALS 3      #
 #################################
@bot.message_handler(commands=['subircg3'])
def subircg3(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame el texto Community Goal 3 con Markdown')
        userStep[m.from_user.first_name] = 'comandantecg3'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")

@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandantecg3', content_types=['text'])
def archivocg3(m):
    cid = m.chat.id
    msg = m.text
    with open('cg3.txt', 'wb') as docu:
        docu.write(msg.encode('utf-8') )
    bot.send_message(m.chat.id,'Community Goal 3 Actualizado.')
    bot.send_message(11186174, "[AVISO] Community Goal 3 Actualizado " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
    userStep[m.from_user.first_name] = 0
    pass
 #################################            
 #        COMMUNITY GOALS 4      #
 #################################
@bot.message_handler(commands=['subircg4'])
def subircg4(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame el texto Community Goal 4 con Markdown')
        userStep[m.from_user.first_name] = 'comandantecg4'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")

@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandantecg4', content_types=['text'])
def archivocg4(m):
    cid = m.chat.id
    msg = m.text
    with open('cg4.txt', 'wb') as docu:
        docu.write(msg.encode('utf-8') )
    bot.send_message(m.chat.id,'Community Goal 4 Actualizado.')
    bot.send_message(11186174, "[AVISO] Community Goal 4 Actualizado " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
    userStep[m.from_user.first_name] = 0  
    pass
@bot.message_handler(commands=['cg'])
def cg(m):
    cid = m.chat.id
    archivo = open("cg.txt", "r") 
    contenido = archivo.read()
    namsel = -36989419
    if cid > 0:
        bot.send_chat_action(cid, 'typing') 
        bot.send_message(cid, contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        #bot.send_sticker(cid,open("tocho.webp", 'rb'))
    else:
        if cid == namsel:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, contenido, parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO] Community Goal usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        else:
            bot.send_message(cid,"Pulsa aquí para ver la Última Noticia -->[Community Goal](https://telegram.me/GalnetESP_BOT?start=galnet)", parse_mode="Markdown", reply_to_message_id=int(m.message_id), disable_web_page_preview = True)

@bot.message_handler(commands=['publicarcg'])
def publicarcg(m):
    archivo = open("cg.txt", 'r')
    contenido = archivo.read()
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        msg = bot.send_message("@EliteDangerousESP", contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal publicado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        bot.send_message(11186174,"Community Goal publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c"))
        bot.send_message(158789972,"Community Goal publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )
        bot.send_message(4891212,"Community Goal publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )


@bot.message_handler(commands=['cg1'])
def cg1(m):
    cid = m.chat.id
    archivo = open("cg1.txt", "r") 
    contenido = archivo.read()
    namsel = -36989419
    if cid > 0:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal 1 usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        #bot.send_sticker(cid,open("tocho.webp", 'rb'))
    else:
        if cid == namsel:
            bot.send_message(cid,contenido,parse_mode="Markdown")
        else:
            pass

@bot.message_handler(commands=['publicarcg1'])
def publicarcg1(m):
    archivo = open("cg1.txt", 'r')
    contenido = archivo.read()
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        msg = bot.send_message("@EliteDangerousESP", contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal 1 publicado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        bot.send_message(11186174,"Community Goal 1 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c"))
        bot.send_message(158789972,"Community Goal 1 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )
        bot.send_message(4891212,"Community Goal 1 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )


@bot.message_handler(commands=['cg2'])
def cg2(m):
    cid = m.chat.id
    archivo = open("cg2.txt", "r") 
    contenido = archivo.read()
    namsel = -36989419
    if cid > 0:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal 2 usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        #bot.send_sticker(cid,open("tocho.webp", 'rb'))
    else:
        if cid == namsel:
            bot.send_message(cid,contenido,parse_mode="Markdown")
        else:
            pass
        
@bot.message_handler(commands=['publicarcg2'])
def publicarcg2(m):
    archivo = open("cg2.txt", 'r')
    contenido = archivo.read()
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        msg = bot.send_message("@EliteDangerousESP", contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal 2 publicado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        bot.send_message(11186174,"Community Goal 2 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c"))
        bot.send_message(158789972,"Community Goal 2 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )
        bot.send_message(4891212,"Community Goal 2 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )


@bot.message_handler(commands=['cg3'])
def cg3(m):
    cid = m.chat.id
    archivo = open("cg3.txt", "r") 
    contenido = archivo.read()
    namsel = -36989419
    if cid > 0:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal 3 usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        #bot.send_sticker(cid,open("tocho.webp", 'rb'))
    else:
        if cid == namsel:
            bot.send_message(cid,contenido,parse_mode="Markdown")
        else:
            pass
        
@bot.message_handler(commands=['publicarcg3'])
def publicarcg3(m):
    archivo = open("cg3.txt", 'r')
    contenido = archivo.read()
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        msg = bot.send_message("@EliteDangerousESP", contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal 3 publicado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        bot.send_message(11186174,"Community Goal 3 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c"))
        bot.send_message(158789972,"Community Goal 3 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )
        bot.send_message(4891212,"Community Goal 3 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )

        
@bot.message_handler(commands=['cg4'])
def cg4(m):
    cid = m.chat.id
    archivo = open("cg4.txt", "r") 
    contenido = archivo.read()
    namsel = -36989419
    if cid > 0:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal 4 usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        #bot.send_sticker(cid,open("tocho.webp", 'rb'))
    else:
        if cid == namsel:
            bot.send_message(cid,contenido,parse_mode="Markdown")
        else:
            pass        
        
@bot.message_handler(commands=['publicarcg4'])
def publicarcg4(m):
    archivo = open("cg4.txt", 'r')
    contenido = archivo.read()
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        msg = bot.send_message("@EliteDangerousESP", contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal 4 publicado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        bot.send_message(11186174,"Community Goal 4 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c"))
        bot.send_message(158789972,"Community Goal 4 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )
        bot.send_message(4891212,"Community Goal 4 publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )


@bot.message_handler(commands=['modificarcg'])
def modificarcg(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not uid in administrador or len(m.text.split()) != 2:
        return
    msg_id = m.text.split()[1]
    msg_text = open('cg.txt','r').read()
    try:
        bot.edit_message_text(msg_text, "@CanalEliteESP", msg_id, parse_mode="Markdown")
    except Exception as e:
        bot.send_message(cid, e)


@bot.message_handler(commands=['descargarcg'])
def descargarcg(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_document(cid, open("cg.txt", 'rb'))
        bot.send_message(11186174, "[AVISO] Community Goal descargado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        
        
  ####################            
  #      PRUEBAS     #
  ####################        
        
@bot.message_handler(commands=['publicargalnetprueba'])
def publicargalnetprueba(m):
    archivo = open("galnet.txt", 'r')
    contenido = archivo.read()
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message("@pruebagarfield", contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Galnet publicado en prueba por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")



@bot.message_handler(commands=['publicarcgprueba'])
def publicarcgprueba(m):
    archivo = open("cg.txt", 'r')
    contenido = archivo.read()
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        msg = bot.send_message("@pruebagarfield", contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal publicado en prueba por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        bot.send_message(11186174,"Community Goal publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c"))
        bot.send_message(158789972,"Community Goal publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )
        bot.send_message(4891212,"Community Goal publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )


@bot.message_handler(commands=['modificarcgprueba'])
def command_responder(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not uid in administrador or len(m.text.split()) != 2:
        return
    msg_id = m.text.split()[1]
    msg_text = open('cg.txt','r').read()
    try:
        bot.edit_message_text(msg_text, "@pruebagarfield", msg_id, parse_mode="Markdown")
    except Exception as e:
        bot.send_message(cid, e)
        
@bot.message_handler(commands=['publicarprueba'])
def publicardirectoprueba(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame Texto a publicar')
        userStep[m.from_user.first_name] = 'comandantepublicardirectoprueba'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")

@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandantepublicardirectoprueba', content_types=['text'])
def publicardirectoprueba2(m):
    cid = m.chat.id
    msg = m.text
    with open('publicar.txt', 'wb') as docu:
        docu.write(msg.encode('utf-8'))
    userStep[m.from_user.first_name] = 0
    archivo = open("publicar.txt", "r") 
    contenido = archivo.read()
    bot.send_message(m.chat.id,'El texto se publicará en breve.')
    bot.send_message("@pruebagarfield", contenido, parse_mode="Markdown")
    userStep[m.chat.id] = 0

@bot.message_handler(commands=['descargarbot'])
def descargarbot(m):
    cid = m.chat.id
    bot.send_document(cid, open("bot2.py", 'rb'))

bot.polling(none_stop=True)