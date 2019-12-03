import logging
import os
from difflib import get_close_matches
from uuid import uuid4

from telegram import InlineQueryResultCachedAudio
from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

loc = os.path.dirname(os.path.abspath('__Shanisirmodule__'))
clipLocation = f"{loc}\\Assets\\clips"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
updater = Updater(token='<API KEY>', use_context=True)
dispatcher = updater.dispatcher

results = []

with open("file_ids.txt", "r") as ids, open("names.txt", "r") as name:
    file_ids = ids.read().strip().split(',')
    names = name.read().strip().split(',')

assert (len(names) == len(file_ids))
for file_id, name in zip(file_ids, names):
    results.append(InlineQueryResultCachedAudio(
        id=uuid4(),
        audio_file_id=file_id,
        caption=name))


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm an inline bot, @ me in the chatbox and type to get a audio clip")


def helper(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="This bot sends you actual shani sir clips straight from Shanisirmodule! He is savage"
                                  " in groups too! More commands will be added in the future."
                                  " P.S: Download Shanisirmodule from:"
                                  " https://github.com/tmslads/Shanisirmodule/releases")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def secret(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="stop finding secret commands :P")


def inline_clips(update, context):
    query = update.inline_query.query
    if not query:
        return
    else:
        matches = get_close_matches(query, names, n=15, cutoff=0.4)
        index = 0
        while index <= len(matches) - 1:
            for pos, result in enumerate(results):
                if index == len(matches):
                    break
                if matches[index] == result['caption']:
                    results[index], results[pos] = results[pos], results[index]
                    index += 1

        context.bot.answer_inline_query(update.inline_query.id, results[:16])


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


inline_clips_handler = InlineQueryHandler(inline_clips)
dispatcher.add_handler(inline_clips_handler)

help_handler = CommandHandler('help', helper)
dispatcher.add_handler(help_handler)

clip_handler = CommandHandler('secret', secret)
dispatcher.add_handler(clip_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
