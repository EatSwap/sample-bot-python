from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
import os


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


if __name__ == '__main__':
    TOKEN = os.environ['TOKEN']
    updater = Updater(token=TOKEN)
    updater.start_webhook(
        listen="0.0.0.0",
        port=8080,
        url_path=TOKEN,
        webhook_url="https://telegram-sample-bot-xyp6.onrender.com/" + TOKEN
    )
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.idle()
