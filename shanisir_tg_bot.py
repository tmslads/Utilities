import logging
import os
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
updater = Updater(token='<INSERT API KEY HERE>', use_context=True)
dispatcher = updater.dispatcher

results = []


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def clips(update, context):
    clipss = os.listdir(clipLocation)
    for clip in clipss:
        c = context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(f'{clipLocation}\\{clip}', 'rb'),
                                   title=f"{clip[:-4]}")
        results.append(InlineQueryResultCachedAudio(
            id=uuid4(),
            audio_file_id=c['audio']['file_id'],
            caption=c['audio']['title']))


def inline_clips(update, context):
    query = update.inline_query.query
    if not query:
        return
    else:
        matches = (result for result in results if query in result['caption'])
        context.bot.answer_inline_query(update.inline_query.id, matches, next_offset="10")


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


inline_clips_handler = InlineQueryHandler(inline_clips)
dispatcher.add_handler(inline_clips_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

clip_handler = CommandHandler('all', clips)
dispatcher.add_handler(clip_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
