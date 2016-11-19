 #encoding=utf8
import telebot
from telebot import types
import time
import sys
from imp import reload
import urllib3
reload(sys)
from bs4 import BeautifulSoup
import requests
import json
import pymongo
from pymongo import MongoClient


administrador = [11186174, 158789972, 4891212, 37690722]
Pi = 158789972
TOKEN = '225774062:AAG5HTX5uLVjEcbV2iCVQR9MjB-isf4tFB0'
usuarios = [line.rstrip('\n') for line in open('usuarios.txt')] # Cargamos la lista de usuarios.
numeros = [line.rstrip('\n') for line in open('numeros.txt')] # Cargamos la lista de usuarios.
bot = telebot.TeleBot ('225774062:AAG5HTX5uLVjEcbV2iCVQR9MjB-isf4tFB0')
userStep=dict()
urlBase = "http://galnet.cadetesdelespacio.es/"
maxPages = 20
counter = 0

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
@bot.message_handler(commands=['paseo'])
def parseo(m):
    for i in range(1,maxPages):
        # Construyo la URL
        if i > 1:
            url = "%spage/%d/" %(urlBase,i)
        else:
            url = urlBase
    
        # Realizamos la petición a la web
        req = requests.get(url)
        # Comprobamos que la petición nos devuelve un Status Code = 200
        statusCode = req.status_code
        if statusCode == 200:
    
            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            html = BeautifulSoup(req.text)
    
            # Obtenemos todos los divs donde estan las entradas
            entradas = html.find_all('div',{'class':'col-md-4 col-xs-12'})
    
            # Recorremos todas las entradas para extraer el título, autor y fecha
            for entrada in entradas:
                counter += 1
                titulo = entrada.find('span', {'class' : 'tituloPost'}).getText()
                autor = entrada.find('span', {'class' : 'autor'}).getText()
                fecha = entrada.find('span', {'class' : 'fecha'}).getText()
    
                # Imprimo el Título, Autor y Fecha de las entradas
                bot.send_message(m.chat.id, "%d - %s  |  %s  |  %s" %(counter,titulo,autor,fecha))
        else:
            # Si ya no existe la página y me da un 400
            break
############################################
#                DEFINICIONES              #
############################################
def command_galnetprivado(m):
    cid = m.chat.id
    archivo = open("galnet.txt", "r") 
    contenido = archivo.read()
    if cid > 0:
        bot.send_message(cid, contenido)
        bot.send_message(11186174, "[AVISO] Galnet usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")" + " Através de enlace de grupo")

def command_cgprivado(m):
    cid = m.chat.id
    archivo = open("cg.txt", "r")
    contenido = archivo.read()
    if cid > 0:
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
            bot.send_message( cid, "Bienvenido, comandante "+ str(m.chat.first_name) + " o7")
            bot.send_message(11186174 ,"Nuevo Usuario" + "\n" + "Usuario: " + str(name) + str(m.from_user.username) + "\n" + "ID: " + str(cid))
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
        comando = m.text[7:]
        if comando == 'galnet':
            command_galnetprivado(m)
        elif comando == 'cg':
            command_cgprivado(m)
@bot.message_handler(commands=['ayuda'])
def ayuda(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(cid, " #Galnet \n /publicar \n /galnet \n /subirgalnet \n /publicargalnet \n /modificargalnet \n /descargargalnet \n \n #CG \n /cg \n /subircg \n /publicarcg \n /modificarcg \n /descargarcg")
    else:
        bot.send_message(cid, "#Galnet \n /galnet \n \n #CG \n /cg")

@bot.message_handler(commands=['publicar'])
def publicardirecto(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame Texto a publicar')
        userStep[m.from_user.first_name] = 'comandantepublicar'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")
        
        
@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandantepublicar', content_types=['text'])
def publicardirecto2(m):
    cid = m.chat.id
    msg= m.text[9:]
    bot.send_message(m.chat.id,'Galnet Publicado.')
    bot.send_message("@CanalEliteESP", msg, parse_mode="Markdown")
    bot.send_message(11186174, "[AVISO] Galnet Actualizado por " + str(m.from_user.first_name))
    userStep[m.chat.id] = 0

            
  ####################            
  #     GALNET       #
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
        bot.send_message(m.chat.id, 'Enviame el archivo (UTF-8)')
        userStep[m.from_user.first_name] = 'comandante'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")
        
        
@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandante', content_types=['document'])
def allahu_akb(m):
    cid = m.chat.id
    pickgalnet = bot.get_file(m.document.file_id)
    downgalnet = bot.download_file(pickgalnet.file_path)
    with open('galnet.txt','wb') as docu:
        docu.write(downgalnet)
    bot.send_message(m.chat.id,'Galnet Actualizado.')
    bot.send_message(11186174, "[AVISO] Galnet Actualizado por " + str(m.from_user.first_name))
    userStep[m.chat.id] = 0
    
    
@bot.message_handler(commands=['galnet'])
def galnet(m):
    cid = m.chat.id
    archivo = open("galnet.txt", "r") 
    contenido = archivo.read()
    if cid > 0:
        bot.send_message(cid, contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Galnet usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        #bot.send_sticker(cid,open("tocho.webp", 'rb'))
    else:
        bot.send_message(cid,"Pulsa aquí para ver la Última Noticia -->[Galnet](https://telegram.me/GalnetESP_BOT?start=galnet)", parse_mode="Markdown", reply_to_message_id=int(m.message_id), disable_web_page_preview = True)
    
@bot.message_handler(commands=['publicargalnet'])
def publicargalnet(m):
    archivo = open("galnet.txt", 'r')
    contenido = archivo.read()
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        msg = bot.send_message("@CanalEliteESP", contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Galnet publicado en prueba por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
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
    msg_text = open('cg.txt','r').read()
    try:
        bot.edit_message_text(msg_text, "@CanalEliteESP", msg_id, parse_mode="Markdown")
    except Exception as e:
        bot.send_message(cid, e)

@bot.message_handler(commands=['descargargalnet'])
def descargargalnet(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_document(cid, open("galnet.txt", 'rb'))
        bot.send_message(11186174, "[AVISO] Galnet descargado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
            
  ####################            
  #       CG         #
  ####################
  
@bot.message_handler(commands=['subircg'])
def subircg(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame el archivo CG (UTF-8)')
        userStep[m.from_user.first_name] = 'comandantecg'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")
        
        
@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandantecg', content_types=['document'])
def archivocg(m):
    cid = m.chat.id
    pickgalnet = bot.get_file(m.document.file_id)
    downgalnet = bot.download_file(pickgalnet.file_path)
    with open('cg.txt','wb') as docu:
        docu.write(downgalnet)
    bot.send_message(m.chat.id,'Community Goal Actualizado.')
    bot.send_message(11186174, "[AVISO] Community Goal Actualizado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
    userStep[m.chat.id] = 0
    
    
@bot.message_handler(commands=['cg'])
def cg(m):
    cid = m.chat.id
    archivo = open("cg.txt", "r") 
    contenido = archivo.read()
    if cid > 0:
        bot.send_message(cid, contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal usado por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        #bot.send_sticker(cid,open("tocho.webp", 'rb'))
    else:
        bot.send_message(cid,"Pulsa aquí para ver la Última Noticia -->[Community Goal](https://telegram.me/GalnetESP_BOT?start=galnet)", parse_mode="Markdown", reply_to_message_id=int(m.message_id), disable_web_page_preview = True)
    
@bot.message_handler(commands=['publicarcg'])
def publicarcg(m):
    archivo = open("cg.txt", 'r')
    contenido = archivo.read()
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        msg = bot.send_message("@CanalEliteESP", contenido, parse_mode="Markdown")
        bot.send_message(11186174, "[AVISO] Community Goal publicado en prueba por " + str(m.from_user.first_name) + " (" + "@"+ str(m.from_user.username) + ")")
        bot.send_message(11186174,"Community Goal publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c"))
        bot.send_message(158789972,"Community Goal publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )
        bot.send_message(4891212,"Community Goal publicada con la ID: " + str(msg.message_id) +" a las " + time.strftime("%c") )


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
        userStep[m.from_user.first_name] = 'comandantepublicar'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")
        
        
@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandantepublicar', content_types=['text'])
def publicardirectoprueba2(m):
    cid = m.chat.id
    msg= m.text[9:]
    bot.send_message(m.chat.id,'Galnet Publicado.')
    bot.send_message("@pruebagarfield", msg, parse_mode="Markdown")
    bot.send_message(11186174, "[AVISO] Galnet Actualizado por " + str(m.from_user.first_name))
    userStep[m.chat.id] = 0

@bot.message_handler(commands=['descargarbot'])
def descargarbot(m):
    cid = m.chat.id
    bot.send_document(cid, open("bot2.py", 'rb'))

bot.polling(none_stop=True)