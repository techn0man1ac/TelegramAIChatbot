'''
Ukrainian-language Telegram chatbot using artificial intelligence. 
This project is based on LLM Studio, which works as a server for the large language model LLAMA3 8B from META. 
It processes user messages and generates chatbot tokens (responses).

https://github.com/techn0man1ac/TelegramAIChatbot

By Serhii Trush, 2024, MIT License.
'''

import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(message: str):
    logging.error(message)

def loggingMessage(loggMess: str):
    logging.info(loggMess)
