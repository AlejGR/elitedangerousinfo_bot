#encoding=utf8
from config import *

@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in ['Radios'])

@bot.message_handler(commands=['radios'])
def radios(m):
    cid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton("KamocanFM", url="https://kamocan.caster.fm/")
    b2 = types.InlineKeyboardButton("Radio Sidewinder", url="http://www.radiosidewinder.com/listen-now/)")
    b3 = types.InlineKeyboardButton("Lave Radio", url="http://laveradio.com/live/")
    b4 = types.InlineKeyboardButton("Hutton Orbital Radio",url="http://huttonorbital.com/HuttonOrbitalRadio.aspx")
    b5 = types.InlineKeyboardButton("Radio Skvortsov",url="https://www.radionomy.com/es/radio/radioskvortsov/index")
    b6 = types.InlineKeyboardButton("Wasp Radio", url="https://www.radionomy.com/en/radio/waspradio")
    b7 = types.InlineKeyboardButton("Third Rock Radio",url="http://thirdrockradio.rfcmedia.com/")
    b8 = types.InlineKeyboardButton("Soma: Mission Control",url="http://somafm.com/player/#/now-playing/missioncontrol")
    markup.add(b1, b2, b3, b4, b5, b6, b7, b8)
    bot.send_message(cid,":radio: RADIOS DISPONIBLES :radio:", reply_markup=markup)
