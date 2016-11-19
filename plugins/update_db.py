#encoding=utf8
from config import *

@bot.message_handler(commands=['actualizardb'])
def updatedb(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        msg = bot.send_message(administrador, "Descargando NUEVA base de datos")
        urlsistemas = "https://eddb.io/archive/v5/systems.csv"
        #sistemas = requests.get(urlsistemas).csv()
        urlproductos = "https://eddb.io/archive/v4/commodities.json"
        productos = requests.get(urlproductos).json()
        client = MongoClient('localhost:27017')
        db = client.elitedangerous
        bot.edit_message_text("Borrando ANTIGUA base de datos",administrador, msg.message_id)
        db.sistemas.remove()
        db.productos.remove()
        bot.edit_message_text("ACTUALIZANDO nueva base de datos", administrador, msg.message_id)
        try:
            os.popen("rm systems.csv")
            os.popen("wget https://eddb.io/archive/v5/systems.csv")
            os.popen("mongoimport -d elitedangerous -c sistemas --type csv --file systems.csv --headerline")
            for x in productos:
                db.productos.insert(x)
        except:
            bot.edit_message_text("ERROR actualizando la nueva base de datos", administrador, msg.message_id)
        else:
            bot.edit_message_text("ÉXITO actualizando la nueva base de datos", administrador, msg.message_id)
    else:
        bot.send_message(cid, "No Tienes permisos para realizar este comando")
