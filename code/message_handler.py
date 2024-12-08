'''
Ukrainian-language Telegram chatbot using artificial intelligence. 
This project is based on LM Studio, which works as a server for the large language model LLAMA3 8B from META. 
It processes user messages and generates chatbot tokens (responses).

https://github.com/techn0man1ac/TelegramAIChatbot

By Serhii Trush, 2024, MIT License.
'''

import logging
from openai import OpenAI
from config import OPENAI_API_BASE, OPENAI_API_KEY, LLM_MODEL, MAX_TOKENS, BOT_WRITE_TIMEOUT, BOT_TEMPERATURE
from history_handler import load_history_from_file, write_history_to_file
from voice_generator import generate_voice
from command_handler import handle_command, is_voice_on

# OpenAI client configuration
client = OpenAI(base_url=OPENAI_API_BASE, api_key=OPENAI_API_KEY)

def handle_user_message(message, bot, recognized_text=None):
    user_id = message.from_user.id  # Get the user ID from the message
    history = load_history_from_file(user_id)  # Load the chat history for this user from a file
    try:
        user_message = recognized_text if recognized_text else message.text  # Use recognized text or default to message text

        if user_message.startswith('/'):
            user_message = handle_command(user_message, history, user_id)  # Handle commands starting with '/'

        if message.reply_to_message:
            original_message = message.reply_to_message.text  # Get the text of the replied-to message
            user_message = f"«{original_message}»\n{user_message}"  # Append the original message to the user's message

        new_message = {"role": "user", "content": user_message}  # Create a new message object for the user
        history.append(new_message)  # Add the user's message to the chat history
        
        completion = client.chat.completions.create(
            model=LLM_MODEL,  # Specify the model to use
            messages=history,  # Pass the entire chat history to the API
            temperature=float(BOT_TEMPERATURE),  # Set the temperature for response generation
            stream=True,  # Use streaming to receive responses incrementally
            max_tokens=int(MAX_TOKENS),  # Limit the number of tokens in the response
            timeout=int(BOT_WRITE_TIMEOUT)  # Set a timeout for the API call
        )

        new_message = {"role": "assistant", "content": ""}  # Create a new message object for the assistant

        count = 0 # Counter, need to simulate write or voice message make

        for chunk in completion:
            if chunk.choices[0].delta.content:
                new_message["content"] += chunk.choices[0].delta.content  # Append the content of each chunk to the assistant's response
                count += 1
                if count % 8 == 0:  # Update status every 8 characters
                    if is_voice_on(user_id):
                        bot.send_chat_action(message.chat.id, 'record_audio')  # Send an action to indicate voice recording
                    else:
                        bot.send_chat_action(message.chat.id, 'typing')  # Send a typing indicator
        
        if new_message["content"].strip():
            history.append(new_message)  # Add the assistant's response to the chat history
            write_history_to_file(user_id, history)  # Save the updated chat history
            if is_voice_on(user_id): # If voice message
                text_to_voice = new_message["content"]
                voice = generate_voice(text_to_voice, user_id)  # Generate a voice message from text
                bot.send_voice(message.chat.id, voice)  # Send the voice message to the user
                bot.reply_to(message, f'"{text_to_voice}".')  # Show text before convert in voice
                
            else:
                bot.reply_to(message, new_message["content"])  # Reply with the text message
        else:
            history.pop()  # Remove the last message if there's no content
            write_history_to_file(user_id, history)  # Save the updated chat history

    except Exception as e:
        logging.error(f"Error wokr with OpenAI: {e}")  # Log any errors that occur during interaction with the API
        bot.reply_to(message, "Вибачте, сталася помилка. Спробуйте ще раз.")  # Send an apology message to the user
