import functions
from telegram.ext import Updater

def main():
    # Call the logs function to start logging.
    functions.logs()

    # Create the Updater and pass the bot token.
    f = open("TOKEN", "r")
    TOKEN=f.readline().rstrip()
    f.close()
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    # Call the function that contains the handlers for the commands.
    functions.handlers(updater, dispatcher)

# Rock it
main()