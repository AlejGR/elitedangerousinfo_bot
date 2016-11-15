#encoding=utf8
from plugins_dev import *

@bot.message_handler(commands=['setversion'])
def setversion(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in administrador:
        bot.send_message(m.chat.id, 'Enviame la Versión')
        userStep[m.from_user.first_name] = 'comandante'
    else:
        bot.send_message(cid, "Comandante, usted no tienes permisos para realizar esta acción.")

@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandante', content_types=['text'])
def setversionstep(m):
    cid = m.chat.id
    msg = m.text[:20]
    with open('../extra/version_dev.txt', 'wb') as docu:
        docu.write(msg.encode('utf-8'))
    bot.send_message(m.chat.id,'Versión Actualizada.')
    userStep[m.from_user.first_name] = 0
