from telegram.ext import Updater, CommandHandler
from config import token 
import time

def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    time_handler = CommandHandler('time', get_time)
    date_handler = CommandHandler('date', get_date)
    dp.add_handler(time_handler)
    dp.add_handler(date_handler)
    updater.start_polling()
    updater.idle()

def get_time(update, context):
    time_text = time.strftime("%H:%M:%S", time.localtime())
    update.message.reply_text(time_text)

def get_date(update, context):
    date_text = time.strftime("%d/%m/%Y", time.localtime())
    update.message.reply_text(date_text)

if __name__ == '__main__':
    main()