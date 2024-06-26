# Україномовний Telegram чатбот з ШІ

![Copilot_Generated_Bot_Image](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/CopilotGeneratedBotImage.jpg)

Україномовний чат бот з використанням штучного інтелекту. Цей проєкт базується на LLM Studio, яка працює як сервер для великої мовної моделі LLAMA3 8B від компанії META. 

# Особливості

![Voice_conversations_mode](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/conversationVoice.png)

Цей чат бот може як генерувати текстові, так і аудіоповідомленя українською мовою. Синтез та розпізнавання мовлення реалізовано за допомогою сервісів від Google:
- SpeechRecognition: https://pypi.org/project/SpeechRecognition/
- gTTS (Google Text-to-Speech): https://pypi.org/project/gTTS/

В якості інтерфейсу з ШІ я використав меседжер Telegram, це зручно тому, що маєш доступ з сматфону до свого власного ШІ в любому місці, де є інтернет. 
Ось посилання на Telegram API: https://core.telegram.org/bots/api

Для роботи з Telegram API використовується бібліотека pyTelegramBotAPI: https://pypi.org/project/pyTelegramBotAPI/

![Context](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/context.png)

Контекст розмови(вміст переписки з чатботом) зберігається у JSON файл на диск, щоб навіть після перезавантаження скрипта бот "пам'ятав" про що Ви розмовляли з ним раніше.

# Структура проєкту
