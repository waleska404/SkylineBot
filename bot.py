# importa la API de Telegram
from telegram.ext import Updater, CommandHandler

from telegram import ParseMode

from skyline import Skyline

import pickle

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

def createSkyline(update, context):
    print("entro en la func createSkyline")
    id = str(context.args[0])
    print("pillo el primer arg")
    x = int(context.args[1])
    print("pillo el sec arg")
    y = int(context.args[2])
    print("pillo el terc arg")
    x2 = int(context.args[3])
    print("pillo el quart arg")

    s = Skyline(id, x, y, x2)
    print("creo skyline")

    s.plotProcessing()
    print("hago el plotProcessing")

    id2 = id + '.png'
    print(id2)
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(id2,'rb'))
    print("supuestamente despues de enviar el mensaje")

def save(update, context):
    id = str(context.args[0])
    s = Skyline(id, x, y, x2)
    filename = id +'.sky'
    outfile = open(filename, 'wb')
    pickle.dump(s,outfile)
    outfile.close()

def load(update, context):
    id = str(context.args[0])
    filename = id + '.sky'
    infile = open(filename, 'rb')
    s = pickle.load(infile)
    infile.close()

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))

dispatcher.add_handler(CommandHandler('createSkyline', createSkyline))

#dispatcher.add_handler(CommandHandler('lst', lst))
#dispatcher.add_handler(CommandHandler('clean', clean))
#dispatcher.add_handler(CommandHandler('save', save))
#dispatcher.add_handler(CommandHandler('load', load))


# engega el bot
updater.start_polling()
