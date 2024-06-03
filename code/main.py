'''
main.py

project/
│
├── config.py
├── command_handler.py
├── error_handling.py
├── history_handler.py
├── main.py
├── message_handler.py
├── voice_generator.py
├── voice_recognition.py
├── ui.py

'''

import logging
import telebot
from message_handler import handle_user_message
from config import BOT_TOKEN
from error_handling import log_error
from voice_recognition import recognize_voice_message

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['text', 'voice'])
def message_handler(message):
    if message.content_type == 'text':
        handle_user_message(message, bot)
    elif message.content_type == 'voice':
        recognize_voice_message(message, bot)

def main():
    try:
        bot.infinity_polling()
    except Exception as e:
        error_message = f"Помилка під час виконання головного циклу бота: {e}"
        log_error(error_message)

if __name__ == "__main__":
    main()
