'''
Ukrainian-language Telegram chatbot using artificial intelligence. 
This project is based on LM Studio, which works as a server for the large language model LLAMA3 8B from META. 
It processes user messages and generates chatbot tokens (responses).

https://github.com/techn0man1ac/TelegramAIChatbot

By Serhii Trush, 2024, MIT License.
'''

from pydub import AudioSegment, utils
import speech_recognition as sr
from error_handling import log_error, loggingMessage
import io

chunksDurations = 45 # 45 seconds
recognitionLanguage = 'uk-UA' # Language recognition

# Function to recognize speech from a WAV file
def recognize_speech(audio_file):
    recognizer = sr.Recognizer()  # Initialize the speech recognition object
    try:
        textRecognize = "" # Recognize result write here
        audio = AudioSegment.from_file(io.BytesIO(audio_file)) # open audio from buffer
        chunks = utils.make_chunks(audio, chunksDurations * 1000) # separate audio to every "chunksDurations" seconds -> new audio peace
        
        for audioChunk in range(len(chunks)): # every 60 second new iteration
            buffer = io.BytesIO() # use IO buffer for long audios 
            chunks[audioChunk].export(buffer, format="wav") # recognize_google need wav format
            buffer.seek(0)
            with sr.AudioFile(buffer) as source:
                audioRecord = recognizer.record(source)  # Record the audio from the file
            textRecognize += recognizer.recognize_google(audioRecord, language=recognitionLanguage) + " "
            # Recognize speech using Google and every cycle add text recognition
        return textRecognize
    
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
        file_ogg = bot.download_file(file_path)  # Download to buffer voice message in OGG format
        recognized_text = recognize_speech(file_ogg)  # Recognize text from the audio file
        if recognized_text:
            bot.reply_to(message, f'"{recognized_text}".')  # Show text before convert in voice
            handle_user_message(message, bot, recognized_text)  # Handle the text message
        else:
            bot.reply_to(message, "Аудіо не розпізнано.")  # Notify of failure in recognition
    
    except Exception as e:
        log_error(f"Error during voice message recognition: {e}")  # Log an error during voice message recognition
        bot.reply_to(message, "An error occurred while processing the voice message.")  # Notify user of the error
