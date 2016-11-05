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



TOKEN = '180904359:AAEB0HUi2dkuM-IfIis7beISFWTmOTuiEl8'
bot = telebot.TeleBot ('180904359:AAEB0HUi2dkuM-IfIis7beISFWTmOTuiEl8')


msg = bot.send_message(11186174, "Descargando NUEVA base de datos")
url = "https://eddb.io/archive/v4/systems.json"
sistemas = requests.get(url).json()
client = MongoClient('localhost:27017')
db = client.elitedangerous
bot.edit_message_text("Borrando ANTIGUA base de datos")
db.sistemas.remove()
bot.send_message("ACTUALIZANDO nueva base de datos", 11186174, msg.message_id)
try:
    for x in sistemas:
        db.sistemas.insert(x)
except:
    bot.send_message("ERROR actualizando la nueva base de datos", 11186174, msg.message_id)
else:
    bot.send_message("ÉXITO actualizando la nueva base de datos", 11186174, msg.message_id)