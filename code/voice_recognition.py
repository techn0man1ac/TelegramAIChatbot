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

# Function to recognize speech from a WAV file
def recognize_speech(wav_file_path):
    recognizer = sr.Recognizer()  # Initialize the speech recognition object
    try:
        with sr.AudioFile(wav_file_path) as source:
            audioRecord = recognizer.record(source)  # Record the audio from the file
        text = recognizer.recognize_google(audioRecord, language='uk-UA')  # Recognize speech using Google
        return text
    
    except Exception as e:
        loggingMessage(f"Error in speech recognition: {e}")  # Log the error
        return None

# Function to handle voice messages from users
def recognize_voice_message(message, bot):
    # Import handle_user_message here to avoid circular imports
    from message_handler import handle_user_message
    
    try:
        loggingMessage(f"Received voice message")  # Log the receipt of a voice message
        file_id = message.voice.file_id  # Get the file ID of the voice message
        loggingMessage(f"Downloading voice message with file_id: {file_id}")  # Log the download process
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        file_ogg = bot.download_file(file_path)  # Download the voice message in OGG format
        
        user_dir = f"{HISTORY_DIR}{message.from_user.id}/"  # Create a directory for the user
        os.makedirs(user_dir, exist_ok=True)

        ogg_file_path = f"{user_dir}input_temp.ogg"  # Path to the temporary OGG file
        with open(ogg_file_path, 'wb') as f:
            f.write(file_ogg)  # Save the downloaded file
        loggingMessage(f"Download file {ogg_file_path}")

        audio = AudioSegment.from_ogg(ogg_file_path)  # Convert OGG to WAV
        wav_file_path = f"{user_dir}input_temp.wav"
        audio.export(wav_file_path, format="wav")
        loggingMessage(f"Convert OGG to WAV {wav_file_path}")

        recognized_text = recognize_speech(wav_file_path)  # Recognize text from the audio file
        if recognized_text:
            bot.reply_to(message, f'"{recognized_text}".')  # Reply to the user with the recognized text
            handle_user_message(message, bot, recognized_text)  # Handle the text message
        else:
            bot.reply_to(message, "Unable to recognize speech.")  # Notify of failure in recognition
    
    except Exception as e:
        log_error(f"Error during voice message recognition: {e}")  # Log an error during voice message recognition
        bot.reply_to(message, "An error occurred while processing the voice message.")  # Notify user of the error

    finally:
        if os.path.exists(ogg_file_path):
            os.remove(ogg_file_path)  # Delete the temporary OGG file
            loggingMessage(f"Delete temporary file {ogg_file_path}")
        if os.path.exists(wav_file_path):
            os.remove(wav_file_path)  # Delete the temporary WAV file
            loggingMessage(f"Delete temporary file {wav_file_path}")
