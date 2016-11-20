#encoding=utf8
from config import *

@bot.message_handler(commands=['privado'])
def command_responder(m):
    cid = m.chat.id # Al igual que el comando de difundidos, este tiene seguridad.
    uid = m.from_user.id
    if uid == administrador:
        mensajeA = m.text[9:] # En 'mensajeA' almacenamos el texto que hay a la izquierda del comando.
        mensajeID = mensajeA.split(" ")[0] # En 'mensajeID' estamos almacenando la primera palabra de 'mensajeA', que es el ID al cual mandamos el mensaje.
        mensajeB = mensajeA.replace(mensajeID, '') # En 'mensajeB', cogemos 'mensajeA' y le quitamos el ID.
        try: # Intentamos enviarlo.
        	bot.send_message( mensajeID, mensajeB)
        except Exception: # En caso de fallo, avisamos del error.
        	enviar = "-> [" + str(mensajeID) + "]: ERROR enviando mensaje privado."
        else: # En caso de acierto, avisamos del éxito.
            enviar = "-> [" + str(mensajeID) + "]: ÉXITO enviando mensaje privado."
        bot.send_message( cid, enviar)
    else:
        if cid > 0 :
            bot.send_message( administrador, str(m.chat.first_name) + " [" + str(cid) + "] Ha intentado usar el comando para enviar mensajes personales.")
        else:
            bot.send_message( administrador, str(m.from_user.first_name) + " [" + str(cid) + "] Ha intentado usar el comando para enviar mensaje personales.")
