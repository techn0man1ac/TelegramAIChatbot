[![UA_version_README](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/Flags/UA%402x.png)](https://github.com/techn0man1ac/TelegramAIChatbot/)
[![GB_version_README](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/Flags/GB%402x.png)](https://github.com/techn0man1ac/TelegramAIChatbot/blob/main/README_EN.md)

# Україномовний Telegram чат-бот з ШІ

![Copilot_Generated_Bot_Image](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/CopilotGeneratedBotImage.jpg)
> Обгортку проєкту згенеровано з допомогою Copilot у Windows, оригінал зображення обгортки знаходиться [тут](https://www.bing.com/images/create/tech01aibot-telegram-bot-image-with-the-text-27hell/1-66376f0c15b14dce9b8543e76374b77a?id=%2ffnQhXHy14ZA7U%2bG1mpTTg%3d%3d&view=detailv2&idpp=genimg&idpclose=1&thId=OIG2.0xK8wnUzR5ppwvD_Vfi3&frame=sydedg&FORM=SYDBIC).

Україномовний Telegram чат-бот з використанням штучного інтелекту. Цей проєкт базується на LLM Studio, яка працює як сервер для великої мовної моделі LLAMA3 8B від компанії META. Саме вона займається обробкою користувацьких повідомлень та генерацією токенів(відповідей) чат-боту.

# Особливості

Цей чат-бот може як генерувати текстові, так і аудіоповідомленя українською мовою. Синтез та розпізнавання мовлення реалізовано за допомогою бібліотек для Python від Google:
- SpeechRecognition: https://pypi.org/project/SpeechRecognition/
- gTTS (Google Text-to-Speech): https://pypi.org/project/gTTS/

В якості інтерфейсу взаємодії з штучним інтелектом, я використав меседжер Telegram, це зручно тому, що маєш доступ з сматфону до свого власного ШІ в любому місці, де є інтернет. 

![Voice_conversations_mode](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/conversationVoice.png)

Ось посилання на Telegram API: https://core.telegram.org/bots/api

Для роботи з Telegram API використовується бібліотека pyTelegramBotAPI: https://pypi.org/project/pyTelegramBotAPI/

Контекст розмови, а саме вміст змінної `history` у файлі `message_handler.py`(переписки з чат ботом) зберігається в JSON форматі(каталог `conversations/id_Telegram_користувача/current_history.json`) на диск, щоб навіть після перезавантаження скрипта бот "пам'ятав" про що Ви розмовляли з ним раніше.

![Context](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/context.png)

Для реалізації читання структури JSON використана стандартна бібліотека: https://docs.python.org/uk/3/library/json.html

Для роботи з великою мовною моделью використовується 2 елементи програмного забезпечення, а саме бібліотека від OpenAI, яка в свою чергу взаємодіє з LLM Studio.
- Працювати з API від OpenAI на мові Python можна з використаннім бібліотеки, ось посилання: https://pypi.org/project/openai/
Ця бібліотека має широкий функціонал для роботи з ШІ, за цю зручність я вибрав її для свого проєкту чат-боту. Хоча вона і призначена для роботи з продуктами компанії OpenAI, але її також можна використовувати для інших проєктів, наприклад LLM Studio.
- LLM Studio - зручний інструмент з графічним інтерфейсом(GUI), він крорисний для старту роботи з великими мовними моделями(LLM), ось тут можна скачати під Вашу операційну систему: https://lmstudio.ai/

![LLM_Studio](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LLM_Studio.png)

# Версії бібліотек на момент розробки

- telebot == 0.0.5
- openai == 1.33.0
- gTTS == 2.5.1
- SpeechRecognition == 3.10.4
- librosa == 0.10.2.post1
- soundfile == 0.12.1

# Встановлення та налаштування ПЗ

Після встановлення LLM Studio треба скачати LLM, для свого проєкту, в якості ШІ, я використав LLAMA3 на 8 мільярдів параметрів(8B) від компанії META: https://llama.meta.com/llama3/

Щоб встановити велику мовну модель в свою систему потрібно її скачати в LLM Studio, для цього робимо наступні кроки:

![LLM_Studio_LLAMA3_Download](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LLM_Studio_LLAMA3_Download.png)

1. Натискаємо кнопку пошуку.
2. Пишемо у полі пошуку назву потрібної LLM, у моєму випадку це `Llama 3 8B Instruct`
3. Скачуємо. Доступні різні версії квантування(стиснення інформації яка зберігається в LLM), пропоную почати з `Q4_K_M` - золота середина між швидкодією та якістю відповідей. Для більш продуктивніших комп'ютерів є "Q8" або "fp32" версії.

Після завантаження великої мовної моделі тиснемом кнопку `Local Server` - запускаємо сервер, який забезпечить можливість "спілкуватись" з LLM використовуючи локальний сервер за адресою `http://localhost:1234/v1` або `http://localhost:1234/v1/chat/completions`.

![LLM_Studio_LocalServerStart](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LLM_Studio_LocalServerStart.png)

Після налаштування програмного забезпечення потрібно отримати API-ключ, ось чудова стаття як це можна зробити: https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/

![TelegramBotFather](https://github.com/techn0man1ac/TelegramAIChatbot/blob/main/imgs/TelegramBotFather.png)

Наступним кроком є прописати API-ключ, який отримали від `@botfather` в коді файлу `config.py` або для зручності можна всі параметри можна ввести виконавши скрипт  `ui.py`.

![BotConfigUserInterface](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/BotConfigUserInterface.png)

1. Відкрити файл `config.py` тим самим задавши абсолютну адресу до робочого каталогу з проєктом.
2. Скопіювати API-ключ(змінити розкладку клавіатури на "eng", це важливо). А також важливо у поле `HISTORY_DIR` скопіювати абсолютний шлях до каталогу `conversations`, наприклад `C:\Projects\TelegramAIChatbot\conversations\`.
3. Зберегти конфігурацію у файл `config.py` натиснувши кнопку.
4. Запустити бота з кнопки а не виконавши головний скрипт. Після цього Telegram чат-бот виконає файл `main.py` і все повинно запрацювати - можете написати своєму чат-боту українською мовою.

# Структура проєкту

Проєкт складається з декількох модулів, кожен з яких розділяє окремий функціонал, це зроблено для зручності обслуговування коду в майбутньому. Проєкт має наступну структуру:

- ui.py - Модуль графічного інтерфейсу(GUI) для конфігурування та запуску чат-боту.
- main.py - Головний модуль, котрий ініціалізує Telegram бота та всі інші модулі. Для запуску бота виконайте цей файл командою `python main.py` або `python3 main.py`.
- config.py - Модуль який містить конфігурації для чат боту, такі як API-ключ, шлях до каталогу з історією, температура віповідей, кількість токенів для відповіді та інше. 
- command_handler.py - Модуль обробки користувацьких команд, таких як увімкнення та вимкнення голосового режиму(аудіоповідомлень), старт нової бесіди(очищення файлу з історією), команда перекладу ботом тексту з англійської на українську мову.
- error_handling.py - Модуль у якому відбувається логування помилок.
- history_handler.py - Модуль, для роботи(завантаження та збереження) користувацької переписки, іншими словами історії чату. Використовується ID користувача Telegram для розділення розмов користувачів. Тобто один користувач - окрема історія спілкування. Переписка зберігається за наступним каталогом `conversations/id_Telegram_користувача/` у файл `current_history.json`.
- message_handler.py - Модуль, обробки повідомлень від великої мовної моделі. Використовується бібліотека від OpenAI
- voice_generator.py - Модуль, у якому відбувається генерація тексту(відповіді від LLM) у мовлення(TTS) українською мовою.
- voice_recognition.py - Модуль, де виконуються функції розпізнавання мовлення(з аудіо в текст), українською мовою, для подальної передачі тексту у велику мовну модель, яка у свою чергу генеруватиме відповідь користувачеві.


  ![ProjectStructurePicture](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/ProjectStructure.png)

  # Подяки

  Спасибі ChatGPT за асистування розробки проєкту.
