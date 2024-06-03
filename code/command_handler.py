'''
command_handler.py
'''
from history_handler import load_history_from_file

voice_on = {}

def handle_command(user_message, history, user_id):
    global voice_on
    if user_message == '/start':
        user_message = "Ви - 'Tech01-бот'. Відповідаєте українською мовою. формулюєте свої відповіді коротко і лаконічно. Привітайтесь, та задайте запитання 'Як Вас звати?' та звертайтесь до співрозмовника по імені."
        history.clear()
    elif user_message == '/context':
        user_message = "Ви - 'Tech01-бот'. Відповідаєте українською мовою. Формулюєте свої відповіді коротко і лаконічно. Продовжуйте розвивати розмову, використовуйте ім'я співрозмовника у бесідах з ним"
        history = load_history_from_file(user_id)
    elif user_message == '/translate':
        user_message = "Переклади повідомлення на українську мову"
    elif user_message == '/voice_on':
        voice_on[user_id] = True
        user_message = "Режим генерації голосових повідомлень увімкнено"
    elif user_message == '/voice_off':
        voice_on[user_id] = False
        user_message = "Режим генерації голосових повідомлень вимкнено"
    return user_message

def is_voice_on(user_id):
    return voice_on.get(user_id, False)

