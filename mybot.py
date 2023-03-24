from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
import os

openai_key = process.env.OPENAI_KEY

telegram_key = process.env.TELEGRAM_KEY

# Set up the OpenAI API key
openai.api_key = os.getenv(openai_key)

# Define the function that handles user messages
def handle_message(update, context):
    message = update.message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=50
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

# Create the updater and dispatcher
updater = Updater(token=telegram_key, use_context=True)
dispatcher = updater.dispatcher

# Add the message handler to the dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()
updater.idle()
