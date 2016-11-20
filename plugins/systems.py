#encoding=utf8
from config import *

@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in ['Sistemas'])
@bot.message_handler(commands=['sistemas'])
def command_sistemas(m):
    cid = m.chat.id
    name = m.text
    bot.send_message(cid, "Introduzca el nombre del sistema")
    userStep[m.chat.first_name] = 'sistemas'

@bot.message_handler(func=lambda m: get_user_step(m.chat.first_name) == 'sistemas', content_types=['text'])
def sistemasstep(m):
    if len(m.text) >= 1:
        cid = m.chat.id
        name = m.text[:20]
        userStep[m.from_user.first_name] = 0
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
