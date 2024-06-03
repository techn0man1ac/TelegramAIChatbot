'''
history_handler.py
'''

import json
import os
from config import HISTORY_DIR
from error_handling import log_error

def get_history_file(user_id):
    user_directory = os.path.join(HISTORY_DIR, str(user_id))
    os.makedirs(user_directory, exist_ok=True)
    return os.path.join(user_directory, "current_history.json")

def load_history_from_file(user_id):
    history_file = get_history_file(user_id)
    try:
        with open(history_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        log_error(f"Помилка під час завантаження історії для користувача {user_id}: {e}")
        return []

def write_history_to_file(user_id, history):
    try:
        history_file = get_history_file(user_id)
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
    except Exception as e:
        log_error(f"Помилка під час запису історії для користувача {user_id}: {e}")
