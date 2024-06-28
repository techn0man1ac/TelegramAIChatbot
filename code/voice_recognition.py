'''
Ukrainian-language Telegram chatbot using artificial intelligence. 
This project is based on LLM Studio, which works as a server for the large language model LLAMA3 8B from META. 
It processes user messages and generates chatbot tokens (responses).

https://github.com/techn0man1ac/TelegramAIChatbot

By Serhii Trush, 2024, MIT License.
'''

from config import HISTORY_DIR
from pydub import AudioSegment
import speech_recognition as sr
from error_handling import log_error, loggingMessage
import os

def recognize_speech(wav_file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_file_path) as source:
            audioRecord = recognizer.record(source)
        text = recognizer.recognize_google(audioRecord, language='uk-UA')
        return text
    
    except Exception as e:
        loggingMessage(f"Error in speech recognition: {e}")
        return None

def recognize_voice_message(message, bot):
    # Import handle_user_message here to avoid circular import
    from message_handler import handle_user_message
    try:
        loggingMessage(f"Received voice message")
        file_id = message.voice.file_id
        loggingMessage(f"Downloading voice message with file_id: {file_id}")
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        file_ogg = bot.download_file(file_path)
        user_dir = f"{HISTORY_DIR}{message.from_user.id}/"
        os.makedirs(user_dir, exist_ok=True)

        ogg_file_path = f"{user_dir}input_temp.ogg"
        with open(ogg_file_path, 'wb') as f:
            f.write(file_ogg)
        loggingMessage(f"Download file {ogg_file_path}")

        audio = AudioSegment.from_ogg(ogg_file_path)
        wav_file_path = f"{user_dir}input_temp.wav"
        audio.export(wav_file_path, format="wav")
        loggingMessage(f"Convert OGG to WAV {wav_file_path}")

        recognized_text = recognize_speech(wav_file_path)
        if recognized_text:
            bot.reply_to(message, f'"{recognized_text}".')
            handle_user_message(message, bot, recognized_text)
        else:
            bot.reply_to(message, "Не вдалося розпізнати мовлення.")
    
    except Exception as e:
        log_error(f"Error during voice message recognition: {e}")
        bot.reply_to(message, "Сталася помилка під час обробки голосового повідомлення.")

    finally:
        if os.path.exists(ogg_file_path):
            os.remove(ogg_file_path)
            loggingMessage(f"Delete temporary file {ogg_file_path}")
        if os.path.exists(wav_file_path):
            os.remove(wav_file_path)
            loggingMessage(f"Delete temporary file {wav_file_path}")
