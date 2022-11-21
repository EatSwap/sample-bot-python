from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


if __name__ == '__main__':
    TOKEN = '5489762226:AAEeF5a-WVcERI5DQGMV-OB9RsHfI3z8QYg'
    updater = Updater(token=TOKEN)
    updater.start_webhook(
        listen="0.0.0.0",
        port=8080,
        url_path=TOKEN,
        webhook_url="https://sample-bot-python.onrender.com/" + TOKEN
    )
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.idle()
