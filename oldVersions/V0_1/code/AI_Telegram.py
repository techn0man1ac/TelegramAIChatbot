'''
  Tech01 simple Telegram Chat Bot with IA By Serhii Trush with MIT License.
  https://github.com/techn0man1ac/telegramChatBotIA
  Thank's ChatGPT for help.
  By Tech01 labs 2024.
'''

import telebot
import ollama
import json

# Replace with your desired filename
CONTEXT_FILE = "./conversation_context.txt"

BOT_TOKEN = 'API_TOKEN'
OLLAMA_MODEL = 'llama3'

CONTEXT_WINDOW_SIZE = 16_384 # Tokens
MAX_RESPONSE_LENGHT = 8_192 # Кількість символів для відповіді

bot = telebot.TeleBot(BOT_TOKEN)
conversation_context = []

def load_context_from_file():
    """Завантажити контекст розмови з текстового файлу."""
    global conversation_context
    try:
        with open(CONTEXT_FILE, 'r') as f:
            context_data = json.load(f)
            conversation_context = context_data['context']
    except (FileNotFoundError, json.JSONDecodeError):
        # За замовчуванням використовувати порожній контекст, якщо файл не існує або не може бути розібраний
        pass

def save_context_to_file():
    """Зберегти контекст розмови у текстовий файл."""
    context_data = {'context': conversation_context}
    with open(CONTEXT_FILE, 'w') as f:
        json.dump(context_data, f)

def update_context(new_context):
    """Оновити контекст розмови новими повідомленнями."""
    global conversation_context
    conversation_context.extend(new_context)
    if len(conversation_context) > CONTEXT_WINDOW_SIZE:
        conversation_context = conversation_context[-CONTEXT_WINDOW_SIZE:]

def handle_user_message(message):
    """Обробляти повідомлення користувача."""
    try:
        user_message = message.text
        systemSet = ''

        if user_message == '/start':
            systemSet = 'Ти - "Tech01-бот", відповідай коротко та лаконічно, українською мовою'  # Підказка для представлення штучного інтелекту
            user_message = "Привітайся"
            conversation_context.clear()  # Очистити контекст для нової розмови

        if user_message == '/context':
            systemSet = 'Ти - "Tech01-бот", відповідай коротко та лаконічно, українською мовою'  # Підказка для представлення штучного інтелекту
            user_message = "Ти оновив контекст бесіди"

        if user_message == '/translate':
            user_message = "Переклади будь ласка попереднє повідомлення на українську мову"

        if message.reply_to_message:
            # Витягти текст цитованого повідомлення
            original_message = message.reply_to_message.text
            # Об'єднати цитоване повідомлення та ваше повідомлення для контексту
            user_message = f"{original_message}\n\n{user_message}"

        ollama_response = ollama.generate(model=OLLAMA_MODEL, prompt=user_message, system = systemSet, context = conversation_context)
        ollama_text = ollama_response['response'][:MAX_RESPONSE_LENGHT]
        update_context(ollama_response['context'])
        bot.reply_to(message, ollama_text)

        # Зберегти контекст розмови після кожного повідомлення, але перезаписати файл
        save_context_to_file()

    except Exception as e:
        print(f"Помилка під час взаємодії з Ollama: {e}")
        bot.reply_to(message, "Вибачте, сталася помилка. Спробуйте ще раз.")

@bot.message_handler(func=lambda msg: True)
def message_handler(message):
    """Обробляти вхідні повідомлення."""
    handle_user_message(message)

def main():
    """Запустити бота."""
    # Завантажити контекст розмови з файлу під час запуску
    load_context_from_file()

    bot.infinity_polling()

if __name__ == "__main__":
    main()
