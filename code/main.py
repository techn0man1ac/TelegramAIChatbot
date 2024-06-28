'''
Ukrainian-language Telegram chatbot using artificial intelligence. 
This project is based on LLM Studio, which works as a server for the large language model LLAMA3 8B from META. 
It processes user messages and generates chatbot tokens (responses).

https://github.com/techn0man1ac/TelegramAIChatbot

By Serhii Trush, 2024, MIT License.
'''

import telebot
from message_handler import handle_user_message  # Import the function to handle user messages
from config import BOT_TOKEN  # Import the bot token from config module
from error_handling import log_error, loggingMessage  # Import the function to log errors
from voice_recognition import recognize_voice_message  # Import the function to recognize voice messages

bot = telebot.TeleBot(BOT_TOKEN)  # Initialize the bot with the provided token

@bot.message_handler(content_types=["text", "voice"])  # Define a handler for text and voice messages
def message_handler(message):
    if message.content_type == "text":
        handle_user_message(message, bot)  # Handle text messages
    elif message.content_type == "voice":
        recognize_voice_message(message, bot)  # Handle voice messages

def main():
    try:
        loggingMessage("Bot started polling")  # Log the start of the bot polling
        bot.infinity_polling()  # Start polling for messages
    except Exception as e:
        error_message = f"Error the executing main bot loop: {e}"
        log_error(error_message)  # Log any errors that occur during the bot's execution

if __name__ == "__main__":
    main()
