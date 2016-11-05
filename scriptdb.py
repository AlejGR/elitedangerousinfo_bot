# -*- coding: utf-8 -*-

import json, requests
from pymongo import MongoClient

url = "https://eddb.io/archive/v4/systems.json"
sistemas = requests.get(url).json()
client = MongoClient('localhost:27017')
db = client.elitedangerous
try:
    db.sistemas.remove()
    for x in sistemas:
        db.sistemas.insert(x)
except:
    print("Fallo en la actualización")
else:
    print("Actualización realizada con éxito")