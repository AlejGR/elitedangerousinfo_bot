#!/usr/bin/env python3
from config import *
#################################################
#                    IMPORTS                    #
#################################################
from config import *
import importdir
import sys


importdir.do('plugins', globals())

try:
    bot.send_message(administrador, "@elitedangerous_bot ha sido encendido")
except Exception as e:
    bot.send_message(administrador, str(e))

bot.polling(none_stop=True, interval=0, timeout=3)
