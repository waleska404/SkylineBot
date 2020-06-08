# importa la API de Telegram
import datetime

from telegram.ext import Updater, CommandHandler
from telegram.ext import Filters, MessageHandler

from telegram import ParseMode
from skyline import Skyline

import sys
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor

import os
import pickle


# hace las inicializaciones pertinentes y da la bienvenida
def start(update, context):
    botname = context.bot.username
    username = update.effective_chat.first_name
    missatge = "¡Hola %s, bienvenida al Skyline bot! Yo soy %s, encantada." % (username, botname)
    context.bot.send_message(chat_id=update.effective_chat.id, text=missatge)
    if not os.path.isdir(username):
        os.mkdir(username)


# el bot contesta con una lista de todas las posibles comandas
def help(update, context):
    msg = ''' Puedes interactuar conmigo utilizando los siguientes comandos:
- */start* : Inicia la conversación conmigo.
- */help* : Obten una lista de todos los comandos que me puedes enviar.
- */author* : Información sobre el autor de este bot.
- */lst* : Muestra los identificadores definidos y su correspondiente area.
- */clean* : Borra todos los identificadores definidos.
- */save id* : Guarda un skyline definido con id: id.
- */load id* : Carga un skyline que hayas guardado previamente con id: id.
'''
    context.bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)


# información sobre el autor del bot
def author(update, context):
    mssg = "La autora de este proyecto es Paula Boyano Ivars. Mail: paula.boyano@est.fib.upc.edu."
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=mssg)


# guardar un skyline
def save(update, context):
    root = os.getcwd()
    ide = str(context.args[0])
    username = update.effective_chat.first_name
    path = root + '/' + username + '/'
    if (ide in context.user_data):
        s = context.user_data[ide]
        filename = path + ide + '.sky'
        outfile = open(filename, 'wb')
        pickle.dump(s, outfile)
        outfile.close()
        mssg = "El skyline con identificador '%s' ha sido guardado." % (ide)
    else:
        mssg = "El identificador que estas intentando guardar no está definido."
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=mssg)


# cargar un skyline
def load(update, context):
    ide = str(context.args[0])
    username = update.effective_chat.first_name
    path = './' + username + '/'
    filename = path + ide + '.sky'
    if os.path.isfile(filename):
        infile = open(filename, 'rb')
        s = pickle.load(infile)
        context.user_data[ide] = s
        infile.close()
        mssg = "El skyline con identificador '%s' se ha cargado." % (ide)
    else:
        mssg = "El skyline que estas intentando cargar no ha sido guardado previamente."
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=mssg)


# listar los skylines definidos
def lst(update, context):
    k = (context.user_data).keys()
    if k:
        mssg = 'Los identificadores definidos hasta el momento son:\n'
        for i in k:
            s = context.user_data[i]
            a = s.getArea()
            m = '-> id: ' + str(i) + ', area: ' + str(a) + '\n'
            mssg += m
    else:
        mssg = 'No hay identificadores definidos.'
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=mssg)


# eliminar los skylines definidos
def clean(update, context):
    mssg = 'Los identificadores definidos hasta el momento han sido borrados.'
    (context.user_data).clear()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=mssg)


# ########### NOT COMANDS MESSAGES PROCESSING ######### #

def noCommand(update, context):

    text = update.message.text
    input_stream = InputStream(update.message.text)
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()
    visitor = EvalVisitor(context.user_data)
    s = visitor.visit(tree)

    s.plotProcessing()

    id = s.getID()
    if id == 'NOEXISTE404':
        mssg = 'Ese identificador no está definido.'
    else:
        id2 = id + '.png'
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(id2, 'rb'))
        a = s.getArea()
        h = s.getHeight()
        a = str(a)
        h = str(h)
        mssg = "area: " + a + "\naltura: " + h
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
