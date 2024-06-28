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
import os  # Import the operating system module for file operations

# Generate an audio file from text using Google Text-to-Speech.
def generate_voice(textToSpeech, user_id):
# textToSpeech (str): The text to be converted to speech. 
# user_id (str): Unique identifier for the user.
          
    outSpeechfile = f"{HISTORY_DIR}{user_id}/output_temp.mp3"  # Define the path to the output speech file

    try:
        tts = gTTS(text=textToSpeech, lang='uk', slow=False)  # Create a gTTS object for Ukrainian language
        tts.save(outSpeechfile)  # Save the generated speech to a file
        audioOpen = open(outSpeechfile, 'rb')  # Open the saved audio file in binary mode
        audioOutput = audioOpen.read()  # Read the contents of the audio file
        audioOpen.close()  # Close the audio file
        if os.path.exists(outSpeechfile):     
            os.remove(outSpeechfile)  # Remove the temporary audio file after reading
        return audioOutput  # Return the binary data of the audio file
    
    except Exception as e:
        log_error(f"Помилка під час генерації голосу: {e}")  # Log any errors that occur during the process
        return None  # Return None if an error occurs
