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
        if name.lower() == 'explosivos':
            namet = 'Explosives'
        elif name.lower() == 'combustible de hidrógeno':
            namet = 'Hydrogen Fuel'
        elif name.lower() == 'combustible de hidrogeno':
            namet = 'Hydrogen Fuel'
        elif name.lower() == 'peróxido de hidrógeno':
            namet = 'Hydrogen Peroxide'
        elif name.lower() == 'peróxido de hidrogeno':
            namet = 'Hydrogen Peroxide'
        elif name.lower() == 'oxígeno líquido':
            namet = 'Liquid Oxygen'
        elif name.lower() == 'oxigeno liquido':
            namet = 'Liquid Oxygen'
        elif name.lower() == 'aceite mineral':
            namet = 'Mineral Oil'
        elif name.lower() == 'agentes nerviosos':
            namet = 'Nerve Agents'
        elif name.lower() == 'pesticida':
            namet = 'Pesticides'
        elif name.lower() =='estabilizadores de superficie':
            namet = 'Surface Stabilisers'
        elif name.lower() == '':
            namet = 'Synthetic Reagents'
        elif name.lower() == 'agua':
            namet = 'Water'
        elif name.lower() == 'ropa':
            namet = 'Clothing'
        elif name.lower() == 'tecnología de consumo':
            namet = 'Consumer Technology'
        elif name.lower() == 'tecnologia de consumo':
            namet = 'Consumer Technology'
        elif name.lower() == 'electrodomésticos':
            namet = 'Domestic Appliances'
        elif name.lower() == 'refugio de evacuación':
            namet = 'Evacuation Shelter'
        elif name.lower() == 'equipamiento de supervivencia':
            namet = 'Survival Equipment'
        elif name.lower() == 'algas':
            namet = 'Algae'
        elif name.lower() == 'carne de animales':
            namet = 'Animal Meat'
        elif name.lower() == 'café':
            namet = 'Coffee'
        elif name.lower() == 'cafe':
            namet = 'Coffee'
        elif name.lower() == 'pescado':
            namet = 'Fish'
        elif name.lower() == 'cartuchos de alimentos':
            namet = 'Food Cartridges'
        elif name.lower() == 'frutas y verduras':
            namet = 'Fruit and Vegetables'
        elif name.lower() == 'grano':
            namet = 'Grain'
        elif name.lower() == 'carne sintética':
            namet = 'Synthetic Meat'
        elif name.lower() == 'carne sintetica':
            namet = 'Synthetic Meat'
        elif name.lower() == 'té':
            namet = 'Tea'
        elif name.lower() == 'te':
            namet = 'Tea'
        elif name.lower() == 'compuestos de cerámica':
            namet = 'Ceramic Composites'
        elif name.lower() == 'compuestos de ceramica':
            namet = 'Ceramic Composites'
        elif name.lower() == '':
            namet = 'CMM Composite'
        elif name.lower() == '':
            namet = 'Cooling Hoses'
        elif name.lower() == 'membrana de aislamiento':
            namet = 'Insulating Membrane'
        elif name.lower() == 'meta-aleciones':
            namet = 'Meta-Alloys'
        elif name.lower() == 'meta aleciones':
            namet = 'Meta-Alloys'
        elif name.lower() == '':
            namet = 'Neofabric Insulation'
        elif name.lower() == 'polímeros':
            namet = 'Polymers'
        elif name.lower() == 'polimeros':
            namet = 'Polymers'
        elif name.lower() == 'semiconductores':
            namet = 'Semiconductors'
        elif name.lower() == 'superconductores':
            namet = 'Superconductors'
        elif name.lower() == 'cerveza':
            namet = 'Beer'
        elif name.lower() == 'licor de contrabando':
            namet = 'Bootleg Liquor'
        elif name.lower() == 'licores':
            namet = 'Liquor'
        elif name.lower() == 'narcóticos':
            namet = 'Narcotics'
        elif name.lower() == 'narcoticos':
            namet = 'Narcotics'
        elif name.lower() == 'tabaco':
            namet = 'Tobacco'
        elif name.lower() == 'vino':
            namet = 'Wine'
        elif name.lower() == 'motores articulados' :
            namet = 'Articulation Motors'
        elif name.lower() == 'procesadores atmosféricos':
            namet = 'Atmospheric Processors'
        elif name.lower() == 'procesadores atmosfericos':
            namet = 'Atmospheric Processors'
        elif name.lower() == 'constructores':
            namet = 'Building Fabricators'
        elif name.lower() == 'cosechadoras de cultivos':
            namet = 'Crop Harvesters'
        elif name.lower() == '':
            namet = 'Emergency Power Cells'
        elif name.lower() == 'colector de escape':
            namet = 'Exhaust Manifold'
        elif name.lower() == 'equipamiento geológico':
            namet = 'Geological Equipment'
        elif name.lower() == 'equipamiento geologico':
            namet = 'Geological Equipment'
        elif name.lower() == '':
            namet = 'Heatsink Interlink'
        elif name.lower() == '':
            namet = 'HN Shock Mount'
        elif name.lower() == '':
            namet = 'Magnetic Emitter Coil'
        elif name.lower() == 'equipamiento marino':
            namet = 'Marine Equipment'
        elif name.lower() == 'hornos microbianos':
            namet = 'Microbial Furnaces'
        elif name.lower() == 'extractor mineral':
            namet = 'Mineral Extractors'
        elif name.lower() == '':
            namet = 'Modular Terminals'
        elif name.lower() == '':
            namet = 'Power Converter'
        elif name.lower() == 'generadores de energía':
            namet = 'Power Generators'
        elif name.lower() == 'generadores de energia':
            namet = 'Power Generators'
        elif name.lower() == '':
            namet = 'Power Grid Assembly'
        elif name.lower() == '':
            namet = 'Power Transfer Conduits'
        elif name.lower() == '':
            namet = 'Radiation Baffle'
        elif name.lower() == '':
            namet = 'Reinforced Mounting Plate'
        elif name.lower() == '':
            namet = 'Skimmer Components'
        elif name.lower() == 'unidades de refrigeramiento':
            namet = 'Thermal Cooling Units'
        elif name.lower() == 'purificadores de agua':
            namet = 'Water Purifiers'
        elif name.lower() == 'medicinas avanzadas':
            namet = 'Advanced Medicines'
        elif name.lower() == 'medicinas agrícolas':
            namet = 'Agri-Medicines'
        elif name.lower() == 'medicinas agricolas':
            namet = 'Agri-Medicines'
        elif name.lower() == 'medicinas agricolas':
            namet = 'Agri-Medicines'
        elif name.lower() == 'medicinas básicas':
            namet = 'Basic Medicines'
        elif name.lower() == 'medicinas basicas':
            namet = 'Basic Medicines'
        elif name.lower() == 'estabilizadores de combate':
            namet = 'Combat Stabilisers'
        elif name.lower() == 'potenciadores de rendimiento':
            namet = 'Performance Enhancers'
        elif name.lower() == 'células madre':
            namet = 'Progenitor Cells'
        elif name.lower() == 'celulas madre':
            namet = 'Progenitor Cells'
        elif name.lower() == 'aluminio':
            namet = 'Aluminium'
        elif name.lower() == 'berilio':
            namet = 'Beryllium'
        elif name.lower() == 'bismuto':
            namet = 'Bismuth'
        elif name.lower() == 'cobalto':
            namet = 'Cobalt'
        elif name.lower() == 'cobre':
            namet = 'Copper'
        elif name.lower() == 'galio':
            namet = 'Gallium'
        elif name.lower() == 'oro':
            namet = 'Gold'
        elif name.lower() == 'hafnio 178':
            namet = 'Hafnium 178'
        elif name.lower() == 'indio':
            namet = 'Indium'
        elif name.lower() == 'lantano':
            namet = 'Lanthanum'
        elif name.lower() == 'litio':
            namet = 'Lithium'
        elif name.lower() == 'osmio':
            namet = 'Osmium'
        elif name.lower() == 'paladio':
            namet = 'Palladium'
        elif name.lower() == 'platino':
            namet = 'Platinum'
        elif name.lower() == 'praseodimio':
            namet = 'Praseodymium'
        elif name.lower() == 'samario':
            namet = 'Samarium'
        elif name.lower() == 'plata':
            namet = 'Silver'
        elif name.lower() == 'tantalio':
            namet = 'Tantalum'
        elif name.lower() == 'talio':
            namet = 'Thallium'
        elif name.lower() == 'torio':
            namet = 'Thorium'
        elif name.lower() == 'titanio':
            namet = 'Titanium'
        elif name.lower() == 'uranio':
            namet = 'Uranium'
        elif name.lower() == 'bauxita':
            namet = 'Bauxite'
        elif name.lower() == 'bertrandita':
            namet = 'Bertrandite'
        elif name.lower() == 'bromellita':
            namet = 'Bromellite'
        elif name.lower() == 'coltán':
            namet = 'Coltan'
        elif name.lower() == 'coltan':
            namet = 'Coltan'
        elif name.lower() == 'criolita':
            namet = 'Cryolite'
        elif name.lower() == 'galita':
            namet = 'Gallite'
        elif name.lower() == '':
            namet = 'Goslarite'
        elif name.lower() == 'indita':
            namet = 'Indite'
        elif name.lower() == 'jadeíta':
            namet = 'Jadeite'
        elif name.lower() == 'jadeita':
            namet = 'Jadeite'
        elif name.lower() == 'lepidolita':
            namet = 'Lepidolite'
        elif name.lower() == 'hidróxido de litio':
            namet = 'Lithium Hydroxide'
        elif name.lower() == 'hidroxido de litio':
            namet = 'Lithium Hydroxide'
        elif name.lower() == 'diamante de baja temperatura':
            namet = 'Low Temperature Diamond'
        elif name.lower() == 'hidrato de metano':
            namet = 'Methane Clathrate'
        elif name.lower() == '':
            namet = 'Methanol Monohydrate Crystals'
        elif name.lower() == 'moissanita':
            name = 'Moissanite'
        elif name.lower() == 'painita':
            namet = 'Painite'
        elif name.lower() == 'pirofilita':
            namet = 'Pyrophyllite'
        elif name.lower() == 'rutilo':
            namet = 'Rutile'
        elif name.lower() == 'taaffeite':
            namet = 'Taaffeite'
        elif name.lower() == 'uraninita':
            namet = 'Uraninite'
        a = db.productos.find_one({'name': namet})
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


#############
#  PRUEBAS  #
############# 
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
            bot.send_message( administrador, str(m.from_user.first_name) + " [" + str(cid) + "] Ha intentado usar el comando para enviar mensajes personales.")

@bot.message_handler(commands=['nave'])
def command_naves(m):
    cid = m.chat.id
    if len(m.text.split()) >= 2:
        msg = m.text.split(' ',1)[1]
        msgmin = msg.lower()
        naves = ['adder', 'anaconda', 'asp explorer','cobra mkiii', 'diamondback explorer']
        if msgmin in naves:
            archivo = open("naves/" + str(msgmin) + ".txt", "r") 
            nave = archivo.read()
            bot.send_photo(cid,open("naves/" + str(msgmin) + '.jpg','rb'))
            bot.send_message(cid,nave)
        else:
             bot.send_message(cid, "Esa nave no existe o aún no está en nuestra base de datos.")
    else: 
        bot.send_message(cid, "Te falta el nombre de la nave.")
@bot.message_handler(commands=['navesdisponibles'])     
def navesdisponibles(m):
    cid = m.chat.id
    naves = ['adder', 'anaconda', 'asp explorer', 'cobra mkiii', 'diamondback explorer']
    bot.send_message(cid, "Las naves que se pueden consultar actualmente son:")
    for nave in naves:
        bot.send_message(cid, nave)
        
bot.polling(none_stop=True)