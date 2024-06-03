'''
message_handler.py
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
    user_id = message.from_user.id
    history = load_history_from_file(user_id)
    try:
        user_message = recognized_text if recognized_text else message.text

        if user_message.startswith('/'):
            user_message = handle_command(user_message, history, user_id)

        if message.reply_to_message:
            original_message = message.reply_to_message.text
            user_message = f"«{original_message}» {user_message}"

        new_message = {"role": "user", "content": user_message}
        history.append(new_message)
        
        completion = client.chat.completions.create(
            model=LLM_MODEL,
            messages=history,
            temperature=BOT_TEMPERATURE,
            stream=True,
            max_tokens=MAX_TOKENS,
            timeout = BOT_WRITE_TIMEOUT
        )

        new_message = {"role": "assistant", "content": ""}

        count = 0

        for chunk in completion:
            if chunk.choices[0].delta.content:
                new_message["content"] += chunk.choices[0].delta.content
                count += 1
                if count % 8 == 0: # Every 8 character update status
                    if is_voice_on(user_id):
                        bot.send_chat_action(message.chat.id, 'record_audio')
                    else:
                        bot.send_chat_action(message.chat.id, 'typing')
        
        if new_message["content"].strip():
            history.append(new_message)
            write_history_to_file(user_id, history)
            if is_voice_on(user_id):
                voice = generate_voice(new_message["content"], user_id)
                bot.send_voice(message.chat.id, voice)
            else:
                bot.reply_to(message, new_message["content"])
        else:
            history.pop()
            write_history_to_file(user_id, history)

    except Exception as e:
        logging.error(f"Помилка під час взаємодії з OpenAI: {e}")
        bot.reply_to(message, "Вибачте, сталася помилка. Спробуйте ще раз.")
