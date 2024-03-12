from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters
from telegram import Update

def start(update = Updater, context = CallbackContext):
    update.message.reply_text("Welcome Bot!")

def echo(update = Update, context = CallbackContext):
    update.message.reply_text(update.message.txt)

def main():
    updater = Updater("6877564918:AAGucZVFy6UGqdumwOoutz256y5uojoCckw")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start of my Bot", start))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, echo()))

    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    print('\tSTART of tm.BOT')
    main()