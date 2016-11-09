#encoding=utf8
from config_dev import *

@bot.message_handler(commands=['help'])
def help(m):
    cid = m.chat.id
    uid = m.from_user.id
    a = open("version.txt", 'r')
    version = a.read()
    b = open("./extras/text_help_dev.txt", 'r')
    texto_ayuda = a.read()
    if uid in administrador:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, str(texto_ayuda), parse_mode="Markdown")
            bot.send_message(administrador, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))
        else:
            pass
    else:
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Este bot ofrece Información de Elite Dangerous, los comandos disponibles son: \n /sistemas <Nombre del sistemas> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del sistema buscado.\n /productos <Nombre del producto (en inglés)> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del producto buscado \n /contactar <mensaje> - Este comando está destinado a problemas/sugerencias que ocurran con el bot. \n /radios - Muestra las radios conocidad de Elite Dangerous. \n /nave - muestra la información de la nave que quieras ver. \n /navesdisponibles - muestra las naves disponibles. \n \n" + str(version), parse_mode="Markdown")
            bot.send_message(administrador, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))
        else:
            if cid == namsel:
               bot.send_chat_action(cid, 'typing')
               bot.send_message(cid, "Este bot ofrece Información de Elite Dangerous, los comandos disponibles son: \n /sistemas <Nombre del sistemas> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del sistema buscado.\n /productos <Nombre del producto (en inglés)> (La búsqueda distingue entre mayúsculas y minúsculas) - Muestra la información del producto buscado \n /contactar <mensaje> - Este comando está destinado a problemas/sugerencias que ocurran con el bot. \n /radios - Muestra las radios conocidad de Elite Dangerous. \n /nave - muestra la información de la nave que quieras ver. \n /navesdisponibles - muestra las naves disponibles. \n \n" + str(version), parse_mode="Markdown")
               bot.send_message(administrador, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))
            else:
                pass
