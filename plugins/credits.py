#encoding=utf8
from config import *

@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in ['Creditos'])
bot.message_handler(commands=['creditos'])
def commands_credit(m):
    cid = m.chat.id
    bot.send_message(cid,"Quiero dar las Gracias a la comunidad de Elite Dangerous ESP y a los administrados de esta. \n En especial a @tunotemetas por redactar los textos a @truenox por darme vacacciones pagadas y @edurolp por ayudarme con el bot \n \n CMDR Garfieldrockero ")
