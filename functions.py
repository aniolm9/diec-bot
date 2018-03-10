import commands
import logging
from telegram.ext import CommandHandler, InlineQueryHandler

def logs():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def handlers(updater, dispatcher):
    # start command
    start_handler = CommandHandler('start', commands.start)
    dispatcher.add_handler(start_handler)

    # ajuda command
    ajuda_handler = CommandHandler('ajuda', commands.ajuda)
    dispatcher.add_handler(ajuda_handler)

    # inline bot handler
    dispatcher.add_handler(InlineQueryHandler(commands.inlinequery))

    # error handler
    dispatcher.add_error_handler(error)

    # Start the bot.
    updater.start_polling()

    # Wait for Ctrl-C or other SIGs to end the process gracefully.
    updater.idle()


def error(bot, update, error):
    logger = logs()
    logger.warning('Update "%s" caused error "%s"', update, error)