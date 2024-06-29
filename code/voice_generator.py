'''
Ukrainian-language Telegram chatbot using artificial intelligence. 
This project is based on LLM Studio, which works as a server for the large language model LLAMA3 8B from META. 
It processes user messages and generates chatbot tokens (responses).

https://github.com/techn0man1ac/TelegramAIChatbot

By Serhii Trush, 2024, MIT License.
'''

from gtts import gTTS  # Import the Google Text-to-Speech library
from config import HISTORY_DIR  # Import the path to the chat history directory from a configuration file
from error_handling import log_error  # Import the function to log errors
import io

# Generate an audio file from text using Google Text-to-Speech.
def generate_voice(textToSpeech: str, user_id: int):
# textToSpeech (str): The text to be converted to speech. 
# user_id (int): Unique identifier for the user.

    try:
        tts = gTTS(text=textToSpeech, lang='uk', slow=False)  # Create a gTTS object for Ukrainian language
        buffer = io.BytesIO() # use IO buffer for audio 
        buffer.name = "temp.mp3"
        tts.write_to_fp(buffer)  # Save the generated speech to buffer
        buffer.seek(0)
        audioOutput = buffer.read()  # Read audio file from the buffer
        return audioOutput  # Return the binary data of the audio file
    
    except Exception as e:
        log_error(f"Помилка під час генерації голосу: {e}")  # Log any errors that occur during the process
        return None  # Return None if an error occurs
