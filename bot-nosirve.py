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
admin = [4891212,11186174]
TOKEN = '180904359:AAHR0sl_cjv9bREgCjKWVJ_kNpd3MN14T5E'
usuarios = [line.rstrip('\n') for line in open('usuarios.txt')] # Cargamos la lista de usuarios.
numeros = [line.rstrip('\n') for line in open('numeros.txt')] # Cargamos la lista de usuarios.
bot = telebot.TeleBot ('180904359:AAHR0sl_cjv9bREgCjKWVJ_kNpd3MN14T5E')
markup = types.ForceReply(selective=False)
userStep=dict()
encuesta = {
    'encuesta': '',
    'respuestas' : [],
    }

votaciones = {}

def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            if m.text.lower() == '/sistemas tontopoia':
                bot.send_message(cid, "Nombre del Sistema: tontopoia \nPotencia: Truenox\nEstado: tonto\nAliado: Que va a tener aliados este\nFacción: Asociación de tontospoias sin fronteras \nGobierno: Ninguno\nEconomía Primaria: haser el tonto\nPoblación: -15168621\nCoordenadas: No se sabe")
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
            bot.send_message(11186174,"Nuevo Usuario" + "\n" + "Usuario: " + str(name) + " - " + "@"  + str(m.chat.username) + "\n" + "ID: " + str(cid))
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
            bot.send_message( cid ,"Hola,soy el bot destinado a Elite: Dangerous, encantado de estar en "+ str(m.chat.title))
        else:
            bot.send_message( cid ,"El grupo "+ str(m.chat.title) + " está ya registrado en nuestra base de datos.")
    comando = m.text[7:]
    if comando == 'votar':
        command_empezar(m)

#################################
#           LISTAS              #
#################################
def get_user_step(comandante):
    if comandante in userStep:
        return userStep[comandante]
    return 0
#################################
#        COMANDOS AYUDA         #
#################################


@bot.message_handler(commands=['ayuda'])
def ayuda(m):
    cid = m.chat.id
    uid = m.from_user.id
    a = open("version.txt", 'r')
    version = a.read()
    if uid in administrador:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece Información de Elite Dangerous, los comandos disponibles son: \n /sistemas <Nombre del sistemas> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del sistema buscado. \n /productos <Nombre del producto (en inglés)> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del producto buscado \n /contactar <mensaje> - Este comando está destinado a problemas/sugerencias que ocurran con el bot. \n /radios - Muestra las radios conocidad de Elite Dangerous. \n \n" + str(version), parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))    
        else:
            pass
    else:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece Información de Elite Dangerous, los comandos disponibles son: \n /sistemas <Nombre del sistemas> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del sistema buscado.\n /productos <Nombre del producto (en inglés)> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del producto buscado \n /contactar <mensaje> - Este comando está destinado a problemas/sugerencias que ocurran con el bot. \n /radios - Muestra las radios conocidad de Elite Dangerous. \n \n" + str(version), parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))
        else:
            pass
        
@bot.message_handler(commands=['help'])
def help(m):
    cid = m.chat.id
    uid = m.from_user.id
    namsel = -36989419
    a = open("version.txt", 'r')
    version = a.read()
    if uid in administrador:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece Información de Elite Dangerous, los comandos disponibles son: \n /sistemas <Nombre del sistemas> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del sistema buscado.\n /productos <Nombre del producto (en inglés)> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del producto buscado \n /contactar <mensaje> - Este comando está destinado a problemas/sugerencias que ocurran con el bot. \n /radios - Muestra las radios conocidad de Elite Dangerous. \n \n" + str(version), parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))    
        else:
            pass
    else:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece Información de Elite Dangerous, los comandos disponibles son: \n /sistemas <Nombre del sistemas> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del sistema buscado.\n /productos <Nombre del producto (en inglés)> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del producto buscado \n /contactar <mensaje> - Este comando está destinado a problemas/sugerencias que ocurran con el bot. \n /radios - Muestra las radios conocidad de Elite Dangerous. \n \n" + str(version), parse_mode="Markdown")
            bot.send_message(11186174, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))
        else:
            if cid == namsel:
               bot.send_chat_action(cid, 'typing')
               bot.send_message(cid, "Este bot ofrece Información de Elite Dangerous, los comandos disponibles son: \n /sistemas <Nombre del sistemas> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del sistema buscado.\n /productos <Nombre del producto (en inglés)> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del producto buscado \n /contactar <mensaje> - Este comando está destinado a problemas/sugerencias que ocurran con el bot. \n /radios - Muestra las radios conocidad de Elite Dangerous. \n \n" + str(version), parse_mode="Markdown")
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
with open('commodities.json') as h:
    commodities = json.load(h)

@bot.message_handler(commands=['sistemas'])
def command_sistemas(m):
    cid = m.chat.id
    if len(m.text.split()) >= 2:
        name = m.text.split(' ',1)[1]
        a = db.sistemas.find_one({'name': name})
        if a:
            e = a.get('needs_permit')
            if e == 0:
                y = "No"
            else:
                y = "Sí"
            consulta = "*Nombre del Sistema*: {}\n*Potencia*: {}\n*Estado*: {}\n*Aliado*: {}\n*Facción*: {}\n*Gobierno*: {}\n*Economía Primaria*: {}\n*Población*: {}\n*Necesita Permiso*: {}\n*Coordenadas*:\n \t *X*: {} \n \t *Y*: {} \n \t *Z*: {} ".format(
            a.get('name'),
            a.get('power'),
            a.get('state'),
            a.get('allegiance'),
            a.get('faction'),
            a.get('government'),
            a.get('primary_economy'),
            a.get('population'),
            str(y),
            a.get('x'),
            a.get('y'),
            a.get('z')
            )
        else:
            consulta = "Me da que eso no existe."
    else:
        consulta = "Macho, pon el nombre"
    
    bot.send_message(cid, consulta, parse_mode="Markdown")

@bot.message_handler(commands=['productos'])
def command_productos(m):
    cid = m.chat.id
    if len(m.text.split()) >= 2:
        name = m.text.split(' ',1)[1]
        ##################
        #   TRADUCCIÓN   #
        ##################
        a = db.productos.find_one({'name': name})
        if a:
            e = a.get('is_rare')
            if e == 0:
                y = "No"
            else:
                y = "Sí"
            consulta = "*Nombre del producto*: {}\n*Categoría del Producto*: {}\n*Precio Medio del Producto*: {} Cr\n*Objeto Raro*: {} ".format(
            a.get('name'),
            a.get('category').get('name'),
            a.get('average_price'),
            str(y)
            )
        else:
            consulta = "Me da que ese producto no existe."
    else:
        consulta = "Macho, pon el nombre"
    
    bot.send_message(cid, consulta, parse_mode="Markdown")

@bot.message_handler(commands=['radios'])
def radios(m):
    cid = m.chat.id
    bot.send_message(cid, "*En Español:* \n [KamocanFM](http://kamocan.caster.fm/)\n [Radio Federal](https://www.radionomy.com/en/radio/radiofederal/index) \n \n *En Inglés:*\n [Radio Sidewinder](http://www.radiosidewinder.com/listen-now/) \n [Lave Radio](http://laveradio.com/live/) \n [Hutton Orbital Radio](http://huttonorbital.com/HuttonOrbitalRadio.aspx) \n [Radio Skvortsov](https://www.radionomy.com/es/radio/radioskvortsov/index) \n [Wasp Radio](https://www.radionomy.com/en/radio/waspradio) \n [Third Rock](http://thirdrockradio.rfcmedia.com/) \n [Soma: Mission Control](http://somafm.com/player/#/now-playing/missioncontrol)", parse_mode="Markdown", disable_web_page_preview="True")

@bot.message_handler(commands=['setversion'])
def setversion(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame el archivo (UTF-8)')
        userStep[m.from_user.first_name] = 'comandante'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")

@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandante', content_types=['text'])
def setversionstep(m):
    cid = m.chat.id
    msg = m.text[:20]
    with open('version.txt', 'wb') as docu:
        docu.write(msg.encode('utf-8') )
    bot.send_message(m.chat.id,'Versión Actualizada.')
############################
#       ENCUESTAS          #
############################
@bot.message_handler(commands=['encuesta'])
def command_pregunta(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in admin:
        msg = bot.send_message( cid, "Escribe la pregunta", reply_markup=markup)
        bot.register_next_step_handler( msg, guardaEncuesta)

def guardaEncuesta(m):
    cid = m.chat.id
    uid = m.from_user.id
    if cid in admin:
        encuesta['encuesta'] = m.text
        msg = bot.send_message( cid, "Respuesta 1: ", reply_markup=markup)
        bot.register_next_step_handler( msg, respuestas)

def respuestas(m):
    cid = m.chat.id
    uid = m.from_user.id
    if cid in admin:
        if not m.text.startswith('/fin'):
            nEle = len(encuesta['respuestas']) + 2
            encuesta['respuestas'].append(m.text)
            msg = bot.send_message( cid, "Respuesta " + str(nEle) + ": ", reply_markup=markup)
            bot.register_next_step_handler( msg, respuestas)
        else:
            hideBoard = types.ReplyKeyboardHide()
            bot.send_message( cid, "Encuesta terminada. Enlace para votar: http://telegram.me/elitedangerous_bot?start=votar", reply_markup=hideBoard)

@bot.message_handler(commands=['start'])
def command_empezar(m):
    cid = m.chat.id
    if cid > 0 and m.text == '/start votar' and encuesta['respuestas']:
        markup = types.ReplyKeyboardMarkup()
        markup.resize_keyboard = True
        for respuesta in encuesta['respuestas']:
            markup.add(respuesta)
        msg = bot.send_message( cid, encuesta['encuesta'], reply_markup=markup)
        bot.register_next_step_handler( msg, votar)

def votar(m):
    cid = m.chat.id
    if m.text in encuesta['respuestas']:
        markup = types.ReplyKeyboardHide()
        mensaje = str(m.from_user.first_name) + " (@" + str(m.from_user.username) + ")"
        votaciones[mensaje] = m.text
        bot.send_message( cid, "Voto añadido/actualizado", reply_markup=markup)
        bot.send_message( admin, mensaje + " ha votado.")

@bot.message_handler(commands=['resultados'])
def command_resultados(m):
    cid = m.chat.id
    uid = m.from_user.id
    if cid in admin and votaciones:
        mensaje = ""
        for key in votaciones:
            mensaje += key + ": " + votaciones[key] + "\n"
        bot.send_message( cid, mensaje)
    elif uid in admin and not votaciones:
        bot.send_message( cid, "Aún no ha votado nadie.")

@bot.message_handler(commands=['reset'])
def command_reset(m):
    uid = m.from_user.id
    if uid in admin:
        encuesta['encuesta'] = ''
        encuesta['respuestas'] = []
        votaciones.clear()
        bot.send_message(4891212, "Todo reseteado")
        bot.send_message(11186174, "Todo reseteado")

###################
#  ACTUALIZAR BD  #
################### 

@bot.message_handler(commands=['actualizardb'])
def updatedb(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        msg = bot.send_message(11186174, "Descargando NUEVA base de datos")
        urlsistemas = "https://eddb.io/archive/v4/systems.json"
        sistemas = requests.get(urlsistemas).json()
        urlproductos = "https://eddb.io/archive/v4/commodities.json"
        productos = requests.get(urlproductos).json()
        client = MongoClient('localhost:27017')
        db = client.elitedangerous
        bot.edit_message_text("Borrando ANTIGUA base de datos",11186174, msg.message_id)
        db.sistemas.remove()
        db.productos.remove()
        bot.edit_message_text("ACTUALIZANDO nueva base de datos", 11186174, msg.message_id)
        try:
            for x in sistemas:
                db.sistemas.insert(x)
            for x in productos:
                db.productos.insert(x)
        except:
            bot.edit_message_text("ERROR actualizando la nueva base de datos", 11186174, msg.message_id)
        else:
            bot.edit_message_text("ÉXITO actualizando la nueva base de datos", 11186174, msg.message_id)
################
## UTILIDADES ##
################
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
        
@bot.message_handler(commands=['privado'])
def command_responder(m):
    cid = m.chat.id # Al igual que el comando de difundidos, este tiene seguridad.
    uid = m.from_user.id
    if uid in administrador:
        mensajeA = m.text[9:] # En 'mensajeA' almacenamos el texto que hay a la izquierda del comando.
        mensajeID = mensajeA.split(" ")[0] # En 'mensajeID' estamos almacenando la primera palabra de 'mensajeA', que es el ID al cual mandamos el mensaje.
        mensajeB = mensajeA.replace(mensajeID, '') # En 'mensajeB', cogemos 'mensajeA' y le quitamos el ID.
        try: # Intentamos enviarlo.
        	bot.send_message( mensajeID, mensajeB)
        except Exception: # En caso de fallo, avisamos del error.
        	enviar = "-> [" + str(mensajeID) + "]: ERROR enviando mensaje privado." 
        else: # En caso de acierto, avisamos del éxito.
            enviar = "-> [" + str(mensajeID) + "]: ÉXITO enviando mensaje privado."
        bot.send_message( cid, enviar)
    else:
        if cid > 0 :
            bot.send_message( administrador, str(m.chat.first_name) + " [" + str(cid) + "] Ha intentado usar el comando para enviar mensajes personales.")
        else:
            bot.send_message( administrador, str(m.from_user.first_name) + " [" + str(cid) + "] Ha intentado usar el comando para enviar mensaje personales.")
            

#############
#  PRUEBAS  #
############# 


bot.polling(none_stop=True)