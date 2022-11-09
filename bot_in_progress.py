import telegram
import telegram.ext
import re
from random import randint
from parser_latest import show_latest

# The API Key we received for our bot
API_KEY = "5622509365:AAEyXvYJMad28r0So26WQrFhbXvDQTnfy60"
# Create an updater object with our API Key
updater = telegram.ext.Updater(API_KEY)
# Retrieve the dispatcher, which will be used to add handlers
dispatcher = updater.dispatcher
# Our states, as integers
ABOUT = 0
RELEASES = 1
CANCEL = 2

n = 2
url = "https://whereyouwatch.com/latest-reports/?pg=" + str(n)

# The entry function
def about(update_obj, context):
    # send the welcoming message, and show the keyboard markup (suggested answers)
    first_name = update_obj.message.from_user['first_name']
    update_obj.message.reply_text(show_latest(url, 1),
        reply_markup=telegram.ReplyKeyboardMarkup([['latest', 'previous']], one_time_keyboard=True)
    )
    # go to the RELEASES state
    return RELEASES

def cancel(update_obj, context):
    # get the user's first name
    first_name = update_obj.message.from_user['first_name']
    update_obj.message.reply_text(
        f"Okay, no question for you then, take care, {first_name}!", reply_markup=telegram.ReplyKeyboardRemove()
    )
    return telegram.ext.ConversationHandler.END

# a regular expression that matches latest or previous
latest_previous_regex = re.compile(r'^(latest|previous|l|p)$', re.IGNORECASE)
# Create our ConversationHandler, with only one state
handler = telegram.ext.ConversationHandler(
      entry_points=[telegram.ext.CommandHandler('start', about)],
      states={
            ABOUT: [telegram.ext.MessageHandler(telegram.ext.Filters.regex(latest_previous_regex), about)],
            # RELEASES: [telegram.ext.MessageHandler(telegram.ext.Filters.regex(r'^\d+$'), releases)],
            # CANCEL: [telegram.ext.MessageHandler(telegram.ext.Filters.regex(latest_previous_regex), cancel)],
      },
      fallbacks=[telegram.ext.CommandHandler('cancel', cancel)],
      )
# add the handler to the dispatcher
dispatcher.add_handler(handler)
# start polling for updates from Telegram
updater.start_polling()
# block until a signal (like one sent by CTRL+C) is sent
updater.idle()