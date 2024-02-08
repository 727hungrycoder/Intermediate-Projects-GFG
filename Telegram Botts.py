from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update

# Replace "YOUR_API_TOKEN" with your actual API token obtained from BotFather
updater = Updater(
    token="6842187162:AAGw9a9bnOGz_4r5XKDlKqOoxHgNqUyhkV4", use_context=True
)


def start(update: Update, context):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot. Please write /help to see the commands available."
    )


def help(update: Update, context):
    update.message.reply_text(
        """Available Commands :-
    /youtube - To get the YouTube URL
    /linkedin - To get the LinkedIn profile URL 
    /gmail - To get the Gmail URL 
    /geeks - To get the GeeksforGeeks URL"""
    )


def gmail_url(update: Update, context):
    update.message.reply_text(
        "Your Gmail link here (I am not giving mine one for security reasons)"
    )


def youtube_url(update: Update, context):
    update.message.reply_text("YouTube Link => https://www.youtube.com/")


def linkedIn_url(update: Update, context):
    update.message.reply_text(
        "LinkedIn URL => https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/"
    )


def geeks_url(update: Update, context):
    update.message.reply_text("GeeksforGeeks URL => https://www.geeksforgeeks.org/")


def unknown(update: Update, context):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)


updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("youtube", youtube_url))
updater.dispatcher.add_handler(CommandHandler("help", help))
updater.dispatcher.add_handler(CommandHandler("linkedin", linkedIn_url))
updater.dispatcher.add_handler(CommandHandler("gmail", gmail_url))
updater.dispatcher.add_handler(CommandHandler("geeks", geeks_url))

updater.start_polling()
