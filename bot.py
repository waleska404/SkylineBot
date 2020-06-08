# importa la API de Telegram
import datetime

from telegram.ext import Updater, CommandHandler
from telegram.ext import Filters, MessageHandler

from telegram import ParseMode
from skyline import Skyline

import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from EvalVisitor import EvalVisitor


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

def save(update, context):
    print('entro en save')
    id = str(context.args[0])
    s = context.user_data[id]
    filename = id +'.sky'
    outfile = open(filename, 'wb')
    pickle.dump(s,outfile)
    outfile.close()
    print('salego en save')

def load(update, context):
    print('entro en load')
    id = str(context.args[0])
    filename = id + '.sky'
    infile = open(filename, 'rb')
    s = pickle.load(infile)
    context.user_data[id] = s
    infile.close()
    print('salgo en load')

def lst(update, context):
    k = (context.user_data).keys()
    mssg = 'Los identificadores definidos hasta el momento son: '
    for i in k:
        s = context.user_data[i]
        a = s.getArea()
        m = 'id: ' + str(i) + ', area: ' + str(a)
        mssg += m

    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=mssg)

def clean(update, context):
    print('ENTRO EN CLEAN')
    mssg = 'Los identificadores definidos hasta el momento han sido borrados.'
    (context.user_data).clear()
    print('HE BORRADO EL DICC')
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=mssg)
    print('SALGO DE CLEAN')
    



############ NOT COMANDS MESSAGES PROCESSING ##########

def noCommand(update, context):
    # get the text the user sent
    text = update.message.text
    #print('print 1:')
    #print(text)
    #print('print 1 fin')

    input_stream = InputStream(update.message.text)
    #print('ha hecho input_stream')

    lexer = SkylineLexer(input_stream)
    #print('ha hecho lexer')

    token_stream = CommonTokenStream(lexer)
    #print('ha hecho token_stream')

    parser = SkylineParser(token_stream)
    #print('ha hecho parser')

    tree = parser.root()
    #print('ha hecho tree')

    visitor = EvalVisitor(context.user_data)
    #print('ha hecho visitor')

    s = visitor.visit(tree)
    #print('ha hecho s')
    
    s.plotProcessing()
    #print("hago el plotProcessing")

    id = s.getID()

    #if id == 'null':
     #   id = str(datetime.datetime.now())
     #  id = id.replace(" ","")
     #   id = id.replace(".","")
     #   id = id.replace(":","")
     #   id = id.replace("-","")
    #id = 'plot'
    id2 = id + '.png'
    print(id2)
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(id2,'rb'))
    print("supuestamente despues de enviar el mensaje")
    a = s.getArea()
    print(a, 'area en bot')
    h = s.getHeight()
    print(h, 'height en bot')
    a = str(a)
    h = str(h)
    mssg = "area: " + a + ", altura: " + h
    print(mssg)
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=mssg)





##########################################################

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))

dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('lst', lst))

dispatcher.add_handler(MessageHandler(Filters.text, noCommand))


# engega el bot
updater.start_polling()
