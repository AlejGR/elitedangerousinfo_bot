#encoding=utf8
from config import *

@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in ['Creditos'])
@bot.message_handler(commands=['creditos'])
def commands_credit(m):
    cid = m.chat.id
    bot.send_message(cid,"Quiero dar las Gracias a la comunidad de Elite Dangerous ESP y a los administradores de esta. \n\n En especial a @tunotemetas por redactar los textos,a @cmdt_txus por ceder las configuraciones de Coriolis, a @truenox por darme vacaciones pagadas y @edurolp por ayudarme con el bot. \n \n CMDR Garfieldrockero ")
    bot.send_message(administrador, "[AVISO - INFO] Créditos usado por " + str(m.from_user.first_name))
