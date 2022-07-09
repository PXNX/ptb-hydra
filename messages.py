from telegram import Update
from telegram.ext import CallbackContext

def say_hi(update: Update, _: CallbackContext):
    update.message.reply_text("hi")
