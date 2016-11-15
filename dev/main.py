#!/usr/bin/env python3
from config_dev import *
#################################################
#                    IMPORTS                    #
#################################################
from config_dev import *
import importdir
import sys


importdir.do('plugins_dev', globals())

try:
    bot.send_message(administrador, "@elitedangerous_bot ha sido encendido")
except Exception as e:
    bot.send_message(administrador, str(e))

bot.polling(none_stop=True, interval=0, timeout=3)
