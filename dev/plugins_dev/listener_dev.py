#encoding=utf8
from config_dev import *
import requests
import time

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
