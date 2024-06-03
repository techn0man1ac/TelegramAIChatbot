'''
voice_generator.py
'''

from gtts import gTTS
from config import HISTORY_DIR
from error_handling import log_error

# Оновлена функція generate_voice з параметром user_id
def generate_voice(text, user_id, filename=None):
       
    if filename is None:
        filename = f"{HISTORY_DIR}{user_id}/output_temp.mp3"
    try:
        tts = gTTS(text=text, lang='uk', slow=False)
        tts.save(filename)
        return open(filename, 'rb')
    except Exception as e:
        log_error(f"Помилка під час генерації голосу: {e}")
        return None
