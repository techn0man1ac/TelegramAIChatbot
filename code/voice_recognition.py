'''
voice_recognition.py
'''

import librosa
import soundfile as sf
import speech_recognition as sr
import os
from config import HISTORY_DIR

def convert_mp3_to_wav_librosa(mp3_file_path, wav_file_path):
    try:
        y, sr = librosa.load(mp3_file_path, sr=None)
        sf.write(wav_file_path, y, sr)
    except Exception as e:
        print(f"Помилка під час конвертації: {e}")

def recognize_speech(wav_file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language='uk-UA')
            return text
    except Exception as e:
        print(f"Помилка під час розпізнавання мовлення: {e}")
        return None

def recognize_voice_message(message, bot):
    # Import handle_user_message here to avoid circular import
    from message_handler import handle_user_message
    
    file_id = message.voice.file_id
    file_info = bot.get_file(file_id)
    file = bot.download_file(file_info.file_path)
    mp3_file_path = f"{HISTORY_DIR}{message.from_user.id}/input_temp.mp3"
    with open(mp3_file_path, 'wb') as f:
        f.write(file)
    wav_file_path = f"{HISTORY_DIR}{message.from_user.id}/input_temp.wav"
    convert_mp3_to_wav_librosa(mp3_file_path, wav_file_path)
    recognized_text = recognize_speech(wav_file_path)
    if recognized_text:
        handle_user_message(message, bot, recognized_text)
    else:
        bot.reply_to(message, "Не вдалося розпізнати мовлення.")
    if os.path.exists(mp3_file_path):
        os.remove(mp3_file_path)
    if os.path.exists(wav_file_path):
        os.remove(wav_file_path)
