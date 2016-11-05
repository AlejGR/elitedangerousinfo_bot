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
            name = 'Explosives'
        elif name.lower() == 'combustible de hidrógeno':
            name = 'Hydrogen Fuel'
        elif name.lower() == 'combustible de hidrogeno':
            name = 'Hydrogen Fuel'
        elif name.lower() == 'peróxido de hidrógeno':
            name = 'Hydrogen Peroxide'
        elif name.lower() == 'peróxido de hidrogeno':
            name = 'Hydrogen Peroxide'
        elif name.lower() == 'oxígeno líquido':
            name = 'Liquid Oxygen'
        elif name.lower() == 'oxigeno liquido':
            name = 'Liquid Oxygen'
        elif name.lower() == 'aceite mineral':
            name = 'Mineral Oil'
        elif name.lower() == 'agentes nerviosos':
            name = 'Nerve Agents'
        elif name.lower() == 'pesticida':
            name = 'Pesticides'
        elif name.lower() =='estabilizadores de superficie':
            name = 'Surface Stabilisers'
        elif name.lower() == 'agentes sintéticos':
            name = 'Synthetic Reagents'
        elif name.lower() == 'agentes sinteticos':
            name = 'Synthetic Reagents'
        elif name.lower() == 'agua':
            name = 'Water'
        elif name.lower() == 'ropa':
            name = 'Clothing'
        elif name.lower() == 'tecnología de consumo':
            name = 'Consumer Technology'
        elif name.lower() == 'tecnologia de consumo':
            name = 'Consumer Technology'
        elif name.lower() == 'electrodomésticos':
            name = 'Domestic Appliances'
        elif name.lower() == 'refugio de evacuación':
            name = 'Evacuation Shelter'
        elif name.lower() == 'equipamiento de supervivencia':
            name = 'Survival Equipment'
        elif name.lower() == 'algas':
            name = 'Algae'
        elif name.lower() == 'carne de animales':
            name = 'Animal Meat'
        elif name.lower() == 'café':
            name = 'Coffee'
        elif name.lower() == 'cafe':
            name = 'Coffee'
        elif name.lower() == 'pescado':
            name = 'Fish'
        elif name.lower() == 'cartuchos de alimentos':
            name = 'Food Cartridges'
        elif name.lower() == 'frutas y verduras':
            name = 'Fruit and Vegetables'
        elif name.lower() == 'grano':
            name = 'Grain'
        elif name.lower() == 'carne sintética':
            name = 'Synthetic Meat'
        elif name.lower() == 'carne sintetica':
            name = 'Synthetic Meat'
        elif name.lower() == 'té':
            name = 'Tea'
        elif name.lower() == 'te':
            name = 'Tea'
        elif name.lower() == 'compuestos de cerámica':
            name = 'Ceramic Composites'
        elif name.lower() == 'compuestos de ceramica':
            name = 'Ceramic Composites'
        elif name.lower() == '':
            name = 'CMM Composite'
        elif name.lower() == '':
            name = 'Cooling Hoses'
        elif name.lower() == 'membrana de aislamiento':
            name = 'Insulating Membrane'
        elif name.lower() == 'meta-aleciones':
            name = 'Meta-Alloys'
        elif name.lower() == 'meta aleciones':
            name = 'Meta-Alloys'
        elif name.lower() == '':
            name = 'Neofabric Insulation'
        elif name.lower() == 'polímeros':
            name = 'Polymers'
        elif name.lower() == 'polimeros':
            name = 'Polymers'
        elif name.lower() == 'semiconductores':
            name = 'Semiconductors'
        elif name.lower() == 'superconductores':
            name = 'Superconductors'
        elif name.lower() == 'cerveza':
            name = 'Beer'
        elif name.lower() == 'licor de contrabando':
            name = 'Bootleg Liquor'
        elif name.lower() == 'licores':
            name = 'Liquor'
        elif name.lower() == 'narcóticos':
            name = 'Narcotics'
        elif name.lower() == 'narcoticos':
            name = 'Narcotics'
        elif name.lower() == 'tabaco':
            name = 'Tobacco'
        elif name.lower() == 'vino':
            name = 'Wine'
        elif name.lower() == 'motores articulados' :
            name = 'Articulation Motors'
        elif name.lower() == 'procesadores atmosféricos':
            name = 'Atmospheric Processors'
        elif name.lower() == 'procesadores atmosfericos':
            name = 'Atmospheric Processors'
        elif name.lower() == 'constructores':
            name = 'Building Fabricators'
        elif name.lower() == 'cosechadoras de cultivos':
            name = 'Crop Harvesters'
        elif name.lower() == 'células de energía de emergencia':
            name = 'Emergency Power Cells'
        elif name.lower() == 'celulas de energia de emergencia':
            name = 'Emergency Power Cells'
        elif name.lower() == 'celulas de energía de emergencia':
            name = 'Emergency Power Cells'
        elif name.lower() == 'colector de escape':
            name = 'Exhaust Manifold'
        elif name.lower() == 'equipamiento geológico':
            name = 'Geological Equipment'
        elif name.lower() == 'equipamiento geologico':
            name = 'Geological Equipment'
        elif name.lower() == '':
            name = 'Heatsink Interlink'
        elif name.lower() == '':
            name = 'HN Shock Mount'
        elif name.lower() == 'mineral de emisión magnética':
            name = 'Magnetic Emitter Coil'
        elif name.lower() == 'mineral de emision magnetica':
            name = 'Magnetic Emitter Coil'
        elif name.lower() == 'mineral de emisión magnetica':
            name = 'Magnetic Emitter Coil'
        elif name.lower() == 'equipamiento marino':
            name = 'Marine Equipment'
        elif name.lower() == 'hornos microbianos':
            name = 'Microbial Furnaces'
        elif name.lower() == 'extractor mineral':
            name = 'Mineral Extractors'
        elif name.lower() == 'terminales modulares':
            name = 'Modular Terminals'
        elif name.lower() == 'convertidor de energía':
            name = 'Power Converter'
        elif name.lower() == 'convertidor de energia':
            name = 'Power Converter'
        elif name.lower() == 'generadores de energía':
            name = 'Power Generators'
        elif name.lower() == 'generadores de energia':
            name = 'Power Generators'
        elif name.lower() == '':
            name = 'Power Grid Assembly'
        elif name.lower() == '':
            name = 'Power Transfer Conduits'
        elif name.lower() == '':
            name = 'Radiation Baffle'
        elif name.lower() == '':
            name = 'Reinforced Mounting Plate'
        elif name.lower() == '':
            name = 'Skimmer Components'
        elif name.lower() == 'unidades de refrigeramiento':
            name = 'Thermal Cooling Units'
        elif name.lower() == 'purificadores de agua':
            name = 'Water Purifiers'
        elif name.lower() == 'medicinas avanzadas':
            name = 'Advanced Medicines'
        elif name.lower() == 'medicinas agrícolas':
            name = 'Agri-Medicines'
        elif name.lower() == 'medicinas agricolas':
            name = 'Agri-Medicines'
        elif name.lower() == 'medicinas agricolas':
            name = 'Agri-Medicines'
        elif name.lower() == 'medicinas básicas':
            name = 'Basic Medicines'
        elif name.lower() == 'medicinas basicas':
            name = 'Basic Medicines'
        elif name.lower() == 'estabilizadores de combate':
            name = 'Combat Stabilisers'
        elif name.lower() == 'potenciadores de rendimiento':
            name = 'Performance Enhancers'
        elif name.lower() == 'células madre':
            name = 'Progenitor Cells'
        elif name.lower() == 'celulas madre':
            name = 'Progenitor Cells'
        elif name.lower() == 'aluminio':
            name = 'Aluminium'
        elif name.lower() == 'berilio':
            name = 'Beryllium'
        elif name.lower() == 'bismuto':
            name = 'Bismuth'
        elif name.lower() == 'cobalto':
            name = 'Cobalt'
        elif name.lower() == 'cobre':
            name = 'Copper'
        elif name.lower() == 'galio':
            name = 'Gallium'
        elif name.lower() == 'oro':
            name = 'Gold'
        elif name.lower() == 'hafnio 178':
            name = 'Hafnium 178'
        elif name.lower() == 'indio':
            name = 'Indium'
        elif name.lower() == 'lantano':
            name = 'Lanthanum'
        elif name.lower() == 'litio':
            name = 'Lithium'
        elif name.lower() == 'osmio':
            name = 'Osmium'
        elif name.lower() == 'paladio':
            name = 'Palladium'
        elif name.lower() == 'platino':
            name = 'Platinum'
        elif name.lower() == 'praseodimio':
            name = 'Praseodymium'
        elif name.lower() == 'samario':
            name = 'Samarium'
        elif name.lower() == 'plata':
            name = 'Silver'
        elif name.lower() == 'tantalio':
            name = 'Tantalum'
        elif name.lower() == 'talio':
            name = 'Thallium'
        elif name.lower() == 'torio':
            name = 'Thorium'
        elif name.lower() == 'titanio':
            name = 'Titanium'
        elif name.lower() == 'uranio':
            name = 'Uranium'
        elif name.lower() == 'bauxita':
            name = 'Bauxite'
        elif name.lower() == 'bertrandita':
            name = 'Bertrandite'
        elif name.lower() == 'bromellita':
            name = 'Bromellite'
        elif name.lower() == 'coltán':
            name = 'Coltan'
        elif name.lower() == 'coltan':
            name = 'Coltan'
        elif name.lower() == 'criolita':
            name = 'Cryolite'
        elif name.lower() == 'galita':
            name = 'Gallite'
        elif name.lower() == '':
            name = 'Goslarite'
        elif name.lower() == 'indita':
            name = 'Indite'
        elif name.lower() == 'jadeíta':
            name = 'Jadeite'
        elif name.lower() == 'jadeita':
            name = 'Jadeite'
        elif name.lower() == 'lepidolita':
            name = 'Lepidolite'
        elif name.lower() == 'hidróxido de litio':
            name = 'Lithium Hydroxide'
        elif name.lower() == 'hidroxido de litio':
            name = 'Lithium Hydroxide'
        elif name.lower() == 'diamante de baja temperatura':
            name = 'Low Temperature Diamond'
        elif name.lower() == 'hidrato de metano':
            name = 'Methane Clathrate'
        elif name.lower() == 'cristales de monohidrato de metanol':
            name = 'Methanol Monohydrate Crystals'
        elif name.lower() == 'moissanita':
            name = 'Moissanite'
        elif name.lower() == 'painita':
            name = 'Painite'
        elif name.lower() == 'pirofilita':
            name = 'Pyrophyllite'
        elif name.lower() == 'rutilo':
            name = 'Rutile'
        elif name.lower() == 'taaffeite':
            name = 'Taaffeite'
        elif name.lower() == 'uraninita':
            name = 'Uraninite'
        elif name.lower() == 'reliquias de Ai':
            name = 'Ai Relics'
        elif name.lower() == 'artefactos antiguos':
            name = 'Ancient Artefact'
        elif name.lower() == '':
            name = 'Antimatter Containment Unit'
        elif name.lower() == 'antibióticos':
            name = 'Antiquities'
        elif name.lower() == 'planes de asalto':
            name = 'Assault Plans'
        elif name.lower() == 'caja negra':
            name = 'Black Box'
        elif name.lower() == 'muestras comerciales':
            name = 'Commercial Samples'
        elif name.lower() == '':
            name = 'Data Core'
        elif name.lower() == 'papeles diplomáticos':
            name = 'Diplomatic Bag'
        elif name.lower() == 'correo encriptado':
            name = 'Encrypted Correspondence'
        elif name.lower() == 'almacenamiento de datos encriptados':
            name ='Encrypted Data Storage'
        elif name.lower() == 'químicos experimentales':
            name = 'Experimental Chemicals'
        elif name.lower() == '':
            name = 'Fossil Remnants'
        elif name.lower() == '':
            name = 'Galactic Travel Guide'
        elif name.lower() == 'muestras geológicas':
            name = 'Geological Samples'
        elif name.lower() == '':
            name = 'Hostage'
        elif name.lower() == 'inteligencia militar':
            name = 'Military Intelligence'
        elif name.lower() == 'planes militares':
            name = 'Military Plans'
        elif name.lower() == 'Idolos Misteriosos':
            name = 'Mysterious Idol'
        elif name.lower() == 'cápsula de criogenización ocupada':
            name = 'Occupied CryoPod'
        elif name.lower() == 'cápsula de escape ocupada':
            name = 'Occupied Escape Pod'
        elif name.lower() == 'efectos personales':
            name = 'Personal Effects'
        elif name.lower() == 'prisionero político':
            name = 'Political Prisoner'
        elif name.lower() == 'materiales de investigación prohibidos':
            name = 'Prohibited Research Materials'
        elif name.lower() == '':
            name = 'Prototype Tech'
        elif name.lower() == '':
            name = 'Rare Artwork'
        elif name.lower() == 'trasmisiones rebeldes':
            name = 'Rebel Transmissions'
        elif name.lower() == '':
            name = 'Salvageable Wreckage'
        elif name.lower() == '':
            name = 'Sap 8 Core Container'
        elif name.lower() == '':
            name = 'Scientific Research'
        elif name.lower() == 'muestras científicas':
            name = 'Scientific Samples'
        elif name.lower() == '':
            name = 'Space Pioneer Relics'
        elif name.lower() == 'datos tácticos':
            name = 'Tactical Data'
        elif name.lower() == '':
            name = 'Technical Blueprints'
        elif name.lower() == 'datos de comercio':
            name = 'Trade Data'
        elif name.lower() == 'artefactos desconocido':
            name = 'Unknown Artefact'
        elif name.lower() == '':
            name = 'Unstable Data Core'
        elif name.lower() == 'esclavos imperiales':
            name = 'Imperial Slaves'
        elif name.lower() == 'esclavos':
            name = 'Slaves'
        elif name.lower() == 'catalizadores avanzados':
            name = 'Advanced Catalysers'
        elif name.lower() == 'monitores animales':
            name = 'Animal Monitors'
        elif name.lower() == 'sistemas hidropónicos':
            name = 'Aquaponic Systems'
        elif name.lower() == '':
            name = 'Auto-Fabricators'
        elif name.lower() == '':
            name = 'Bioreducing Lichen'
        elif name.lower() == 'componentes de ordenadores':
            name = 'Computer Components'
        elif name.lower() == 'HE Suits':
            name = 'H.E. Suits'
        elif name.lower() == '':
            name = 'H.E. Suits'
        elif name.lower() == '':
            name = 'Hardware Diagnostic Sensor'
        elif name.lower() == '':
            name = 'Ion Distributor'
        elif name.lower() == 'sistemas de enriquecimiento terrestre':
            name = 'Land Enrichment Systems'
        elif name.lower() == 'equipamiento de diagnóstico medico':
            name = 'Medical Diagnostic Equipment'
        elif name.lower() == '':
            name = 'Micro Controllers'
        elif name.lower() == '':
            name = 'Muon Imager'
        elif name.lower() == '':
            name = 'Nanobreakers'
        elif name.lower() == 'separadores de resonancia':
            name = 'Resonating Separators'
        elif name.lower() == 'robots':
            name = 'Robotics'
        elif name.lower() == 'reguladores estructurales':
            name = 'Structural Regulators'
        elif name.lower() =='':
            name = 'Telemetry Suite'
        elif name.lower() == '':
            name = 'Conductive Fabrics'
        elif name.lower() == 'cuero':
            name = 'Leather'
        elif name.lower() == '':
            name = 'Military Grade Fabrics'
        elif name.lower() == '':
            name = 'Natural Fabrics'
        elif name.lower() == '':
            name = 'Synthetic Fabrics'
        elif name.lower() == 'residuos biológicos':
            name = 'Biowaste'
        elif name.lower() == 'residuos químicos':
            name = 'Chemical Waste'
        elif name.lower() == 'basura':
            name = 'Scrap'
        elif name.lower() == 'residuos tóxicos':
            name = 'Toxic Waste'
        elif name.lower() == 'armas de batalla':
            name = 'Battle Weapons'
        elif name.lower() == 'minas de superficie':
            name = 'Landmines'
        elif name.lower() == 'armas no letales':
            name = 'Non-lethal Weapons'
        elif name.lower() == 'armas personales':
            name = 'Personal Weapons'
        elif name.lower() == 'armadura reactiva':
            name = 'Reactive Armour'
        name = name.title()
        a = db.productos.find_one({'name': name})
        if a:
            name1 = m.text.split(' ',1)[1]
            name2 = name1.title()
            e = a.get('is_rare')
            if e == 0:
                y = "No"
            else:
                y = "Sí"
            consulta = "*Nombre del producto*: {}\n*Categoría del Producto*: {}\n*Precio Medio del Producto*: {} Cr\n*Objeto Raro*: {} ".format(
            str(name2),
            a.get('category').get('name'),
            a.get('average_price'),
            str(y)
            )
        else:
            consulta = "Me da que ese producto no existe, Si crees que este objeto que has buscado existe y esta bien escrito pongase en contacto con nosotros usando /contactar"
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
#          NAVES           #
############################
@bot.message_handler(commands=['nave'])
def command_naves(m):
    cid = m.chat.id
    if len(m.text.split()) >= 2:
        msg = m.text.split(' ',1)[1]
        msgmin = msg.lower()
        naves = ['adder', 'anaconda', 'asp explorer','cobra mkiii', 'diamondback explorer', 'diamondback scout', 'eagle', 'fer-de-lance', 'hauler', 'orca', 'python', 'sidewinder', 'type 6', 'type 7', 'type 9', 'viper mkiii', 'vulture']
        if msgmin in naves:
            archivo = open("naves/" + str(msgmin) + ".txt", "r") 
            nave = archivo.read()
            bot.send_photo(cid,open("naves/" + str(msgmin) + '.jpg','rb'))
            bot.send_message(cid,nave, parse_mode="Markdown")
        else:
             bot.send_message(cid, "Esa nave no existe o aún no está en nuestra base de datos.")
    else: 
        bot.send_message(cid, "Te falta el nombre de la nave.")
        
@bot.message_handler(commands=['navesdisponibles'])     
def navesdisponibles(m):
    cid = m.chat.id
    naves = ['Adder', 'Anaconda', 'Asp explorer','Cobra MkIII', 'Diamondback Explorer', 'Diamondback Scout', 'Eagle', 'Fer-De-Lance', 'Hauler', 'Orca', 'Python', 'Sidewinder', 'Type 6', 'Type 7', 'Type 9', 'Viper MkIII', 'Vulture']
    #bot.send_message(cid, "Las naves que se pueden consultar actualmente son: ")
    bot.send_message(cid,'Las naves disponibles en nuestra base de datos son: \n' + '*' +'\n'.join(naves) + '*', parse_mode="Markdown")


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

@bot.message_handler(commands=['usuarios'])
def usuarioscontar(m):
    uid = m.from_user.id
    cid = m.chat.id
    archivo= open("usuarios.txt", "r")
    contenidousuario = archivo.read()
    lineas = len(open('usuarios.txt').readlines())
    if uid in administrador:
        bot.send_message(cid, contenidousuario + "\n" + 'Nº de usuarios: ' +  str(lineas))


#############
#  PRUEBAS  #
############# 
bot.polling(none_stop=True)