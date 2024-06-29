'''
Ukrainian-language Telegram chatbot using artificial intelligence. 
This project is based on LLM Studio, which works as a server for the large language model LLAMA3 8B from META. 
It processes user messages and generates chatbot tokens (responses).

https://github.com/techn0man1ac/TelegramAIChatbot

By Serhii Trush, 2024, MIT License.
'''

# Dictionary to keep track of voice on status for each user
voice_on = {}

# Function to handle commands from the user
def handle_command(user_message: str, history: str, user_id: int) -> str:
    global voice_on
    new_message = ""
    
    # Start a new conversation
    if user_message == "/start":
        history.clear()
        user_message = "Розпочато нову бесіду. Запитай ім'я твого співрозмовника."
        new_message = {"role": "system", "content": "Ви - 'Віртуальний помічник'. Відповідаєте українською мовою. формулюється свої відповіді коротко і лаконічно. Привітайтесь, та задайте запитання 'Як Вас звати?' Звертайтеся до співрозмовника по імені."}
    
    # Show the current context of the conversation
    elif user_message == "/context":
        user_message = "Підведи коротке резюме текучої бесіди будь ласка. У відповіді звернись до твого співрозмовника по імені"
        new_message = {"role": "system", "content": "Ви - 'Віртуальний помічник'. Відповідаєте українською мовою. Формулюється свої відповіді коротко і лаконічно. Продовжуйте розвивати розмову, використовуйте ім'я співрозмовника у бесідах з ним."}
    
    # Translate the message to Ukrainian
    elif user_message == "/translate":
        user_message = "Переклади повідомлення на українську мову"
    
    # Turn on voice mode for the user
    elif user_message == "/voice_on":
        voice_on[user_id] = True
        user_message = "Увімкнено режим голосових повідомлень"
    
    # Turn off voice mode for the user
    elif user_message == "/voice_off":
        voice_on[user_id] = False
        user_message = "Вимкнено режим голосових повідомлень"

    # Write system messages to the history
    if new_message != "":  
        history.append(new_message)

    return user_message

# Check if voice mode is on for a specific user
def is_voice_on(user_id):
    return voice_on.get(user_id, False)
