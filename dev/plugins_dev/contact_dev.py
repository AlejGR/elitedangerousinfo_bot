#encoding=utf8
from config_dev import *

@bot.message_handler(commands=['contactar'])
def command_contactar(m):
    cid = m.chat.id
    name =m.chat.first_name
    bot.send_message(cid, 'Escriba a continuación el mensaje')
    userStep[m.from_user.first_name] = 'comandante'
    msg = m.text

    @bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'comandante', content_types=['text'])
    def contactarstep(m):
        cid = m.chat.id
        msg = m.text[:20]
        bot.send_message( cid, "Mensaje <" + msg + " > enviado con éxito.")
        bot.send_message( administrador, "*Mensaje*:" + msg  + "\n" + "*Usuario*: " + str(name) + " - " + "@" + str(m.from_user.username) + "\n" + "*ID*: " + str(cid), parse_mode="Markdown")
        userStep[m.from_user.first_name] = 0
