# importa la API de Telegram
from telegram.ext import Updater, CommandHandler

from telegram import ParseMode

# hace las inicializaciones pertinentes y da la bienvenida
def start(update, context):
    botname = context.bot.username
    fullname = update.effective_chat.first_name 
    missatge = "¡Hola %s, bienvenida al Skyline bot! Yo soy %s, encantada." % (fullname, botname)
    context.bot.send_message(chat_id=update.effective_chat.id, text=missatge)

# el bot contesta con una lista de todas las posibles comandas
def help(update, context):
    msg = ''' Puedes interactuar conmigo utilizando los siguientes comandos:
- */start*
- */help*
- */author*
- */lst*
- */clean*
- */save id*
- */load id*
'''
    context.bot.send_message(chat_id=update.message.chat_id, text=msg, \
         parse_mode=ParseMode.MARKDOWN)

def author(update, context):
    mssg = "La autora de este proyecto es Paula Boyano Ivars. Mail: paula.boyano@est.fib.upc.edu."
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=mssg)


# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
#dispatcher.add_handler(CommandHandler('lst', lst))
#dispatcher.add_handler(CommandHandler('clean', clean))
#dispatcher.add_handler(CommandHandler('save', save))
#dispatcher.add_handler(CommandHandler('load', load))


# engega el bot
updater.start_polling()
