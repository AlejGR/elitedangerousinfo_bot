from imp import reload
import urllib3
reload(sys)
import requests
import json
import pymongo
from pymongo import MongoClient
import csv
import plugins_dev

with open("ident_dev.json") as f:
    ident = json.load(f)  #load JSON in varible

#############
#Information#
#############

administrador = ident['administrador'] #ID of Superadmin
admin = ident['admin'] #ID of admins
bot = telebot.TeleBot(ident['TOKEN'])
usuarios = [line.rstrip('\n') for line in open(ident['usuarios'])] #load the file usuario in JSON
numeros = [line.rstrip('\n') for line in open(ident['numeros'])] #load the file numeros in JSON
userStep=dict()

###############
#BASE DE DATOS#
###############
client = MongoClient('localhost:27017')
db = client.elitedangerous
f = open('systems.csv')
systems = csv.reader(f)
with open('commodities.json') as h:
    commodities = json.load(h)

def get_user_step(comandante):
    if comandante in userStep:
        return userStep[comandante]
    return 0

with open('responses.json') as f:
    responses = json.load(f)
