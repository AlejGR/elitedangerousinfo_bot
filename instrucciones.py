#clien
#mongod --smallfiles &
import json
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.elitedangerous # o ed
with open('systems.json') as f:
    systems = json.load(f)
for x in systems:
    db.sistemas.insert(x)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#def eddb(rq):
    url = "https://eddb.io/archive/v4/{}.json"
    if rq not in ['systems','stations','commodities','modules']:
        raise ValueError("The param must be one of this: 'systems', 'stations', 'commodities', 'modules'.")
        return
    r = requests.get(url.format(rq))
    return r.json()