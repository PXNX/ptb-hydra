import os

from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Defaults

from config import CHANNEL, TOKEN
from messages import  say_hi


def main():
    updater = Updater(TOKEN, defaults=Defaults(parse_mode=ParseMode.HTML))

    dp = updater.dispatcher


    dp.add_handler(
        MessageHandler(Filters.text, say_hi))

  #  updater.start_webhook(
   #     "0.0.0.0",
    #    int(os.environ["PORT"]),
     #   TOKEN,
      #  webhook_url=f"https://ptb-i3.herokuapp.com/{TOKEN}",
   # )
    updater.start_polling(
    )
    updater.idle()

if __name__ == '__main__':
    main()
