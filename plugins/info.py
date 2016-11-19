#encoding=utf8
from config import *

@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in ['Informacion'])
bot.message_handler(commands=["info"])
def command_info(m):
cid = m.chat.id
markup = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton("Grupo Telegram", url="https://telegram.me/EliteESP")
item2 = types.InlineKeyboardButton("PayPal", url="https://paypal.me/garfieldrockero")
markup.add(item1,item2)
bot.send_message(cid,"@elitedangerous_bot Dispone de una base de datos con los sistemas del juego Elite Dangerous y de sus productos, también cuenta con una recopilación de la información de las naves y radios de la comunidad. \n El bot ha sido creado para la comunidad de Elite Dangerous. \n @elitedangerous_bot no tienen relación con Elite Dangerous o Frontier Developments. ")
