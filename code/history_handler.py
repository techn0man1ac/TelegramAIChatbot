'''
Ukrainian-language Telegram chatbot using artificial intelligence. 
This project is based on LLM Studio, which works as a server for the large language model LLAMA3 8B from META. 
It processes user messages and generates chatbot tokens (responses).

https://github.com/techn0man1ac/TelegramAIChatbot

By Serhii Trush, 2024, MIT License.
'''

import json
import os
from config import HISTORY_DIR
from error_handling import log_error

# Function to get the path for the user's history file
def get_history_file(user_id):
    # Create a directory for the user if it doesn't exist
    user_directory = os.path.join(HISTORY_DIR, str(user_id))
    os.makedirs(user_directory, exist_ok=True)
    # Return the path to the current history JSON file
    return os.path.join(user_directory, "current_history.json")

# Function to load the user's chat history from a file
def load_history_from_file(user_id):
    history_file = get_history_file(user_id)
    try:
        # Open and read the JSON file containing the user's chat history
        with open(history_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []
    except Exception as e:
        # Log any other errors and return an empty list
        log_error(f"Error load user history {user_id}: {e}")
        return []

# Function to write the user's chat history back to a file
def write_history_to_file(user_id, history):
    try:
        # Get the path for the user's history file
        history_file = get_history_file(user_id)
        # Write the updated history to the JSON file
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
    except Exception as e:
        # Log any errors that occur during writing and return None
        log_error(f"Error write user history {user_id}: {e}")
