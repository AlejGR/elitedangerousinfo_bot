 #encoding=utf-8
 from config import *

 @bot.message_handler(commands=['cancelar'])
 def command_cancelar(m):
     userStep[m.from_user.first_name] = 0
 @bot.message_handler(commands=['cancel'])
 def command_cancel(m):
     userStep[m.from_user.first_name] = 0
