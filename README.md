[![UA_version_README](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/Flags/UA%402x.png)](https://github.com/techn0man1ac/TelegramAIChatbot/)
[![GB_version_README](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/Flags/GB%402x.png)](https://github.com/techn0man1ac/TelegramAIChatbot/blob/main/README_EN.md)

# Україномовний Telegram чат-бот з ШІ

![Copilot_Generated_Bot_Image](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/CopilotGeneratedBotImage.jpg)
> Обгортку проєкту згенеровано з допомогою Copilot у Windows, оригінал зображення обгортки знаходиться [тут](https://www.bing.com/images/create/tech01aibot-telegram-bot-image-with-the-text-27hell/1-66376f0c15b14dce9b8543e76374b77a?id=%2ffnQhXHy14ZA7U%2bG1mpTTg%3d%3d&view=detailv2&idpp=genimg&idpclose=1&thId=OIG2.0xK8wnUzR5ppwvD_Vfi3&frame=sydedg&FORM=SYDBIC).

Україномовний Telegram чат-бот з використанням штучного інтелекту. Цей проєкт базується на LM Studio, яка працює як сервер для великої мовної моделі LLAMA3 8B від компанії META. Саме вона займається обробкою користувацьких повідомлень та генерацією токенів(відповідей) чат-боту.

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

Для роботи з великою мовною моделью використовується 2 елементи програмного забезпечення, а саме бібліотека від OpenAI, яка в свою чергу взаємодіє з LM Studio.
- Працювати з API від OpenAI на мові Python можна з використаннім бібліотеки, ось посилання: https://pypi.org/project/openai/
Ця бібліотека має широкий функціонал для роботи з ШІ, за цю зручність я вибрав її для свого проєкту чат-боту. Хоча вона і призначена для роботи з продуктами компанії OpenAI, але її також можна використовувати для інших проєктів, наприклад LM Studio.
- LM Studio - зручний інструмент з графічним інтерфейсом(GUI), він крорисний для старту роботи з великими мовними моделями(LLM), ось тут можна скачати під Вашу операційну систему: https://lmstudio.ai/

![LLM_Studio](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LLM_Studio.png)

# Бібліотеки які використовуються

У цьому проєкті використовуються кілька ключових бібліотек, ось вони:

- telebot == 0.0.5
- openai == 1.33.0
- gTTS == 2.5.1
- SpeechRecognition == 3.10.4
- pydub == 0.25.1

# Встановлення та налаштування ПЗ

Для початку встановлюємо Python https://www.python.org/downloads/

Далі встановлюємо Git https://git-scm.com/downloads та логінемось там використовуючи GitHub.

Скачуємо репозиторій у потрібний Вам каталог(наприклад «C:\Projects\») командою «git clone», яку прописуємо у командному рядку(CMD):

`git clone https://github.com/techn0man1ac/TelegramAIChatbot.git`

Скачувати можна і без git, тобто без реєстрації, просто скачавши архів репозиторію по ось цьому посиланні: https://github.com/techn0man1ac/TelegramAIChatbot/archive/refs/heads/main.zip

Після завантаження заходимо в каталог «TelegramAIChatbot» далі пишемо у командному рядку `cd TelegramAIChatbot` — переміщення в каталог з файлами проєкту;

Встановлюємо всі необхідні бібліотеки для роботи чат-боту(на скріні нижче):

`pip install -r requirements.txt`

![RequirementsInstall](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/CMD.png)

Може бути так(але не обов'язково), що для роботи бібліотеки(окрім самої бібліотеки) pydub необхідно встановити FFmpeg, ось як його встановити: https://www.editframe.com/guides/how-to-install-and-start-using-ffmpeg-in-under-10-minutes

Після встановлення бібліотек заходимо у каталог «code» командою `cd code` та запускаємо модуль графічного інтерфейсу боту командою `python UI.py`:

![RunUI](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/CMD_RUN.png)

Відкриється графічний інтерфейс з налаштуванням чат-боту:

![BotConfigUserInterface](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/BotConfigUserInterface.png)

На цьому етапі треба зробити наступні кроки:

1) Вибрати шлях до конфігураційного файлу «config.py» кнопкою справа зверху;
2) Коли параметри завантажені(усі поля заповнені), потрібно отримати API ключ у головного Telegram боту. Його можна знайти якщо набрати в Telegram @BotFather( https://t.me/BotFather ) у полі пошуку контактів. Інтерфейс інтуїтивно зрозумілий, створюєте бота даючи йому ім’я, потім заходите в керування ботом та тиснете кнопку отримати API key. Про всяк випадок, лишу це посилання https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/ , там описується спочатку як його отримати(до Python коду).
Важливий нюанс — перед тим як змінювати поле «BOT_TOKEN» `змініть розкладку клавіатури на англійську`, і тоді вставляйте ключ.
3) Після тисніть «Зберегти конфігурацію».
4) Тисніть кнопку «Запустити бот» і в консолі, яка запускається разом з UI.py модулем з’явиться повідомлення, що бот в рантаймі(я йому відправив 2 повідомлення, що видно по логах):

![BotRun](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/BotRun.png)

Після встановлення LM Studio треба скачати LLM, для свого проєкту, в якості ШІ, я використав LLAMA3 на 8 мільярдів параметрів(8B) від компанії META: https://llama.meta.com/llama3/

Щоб встановити велику мовну модель у Вашій системі, вам потрібно завантажити її в LM Studio, для цього достатньо натиснути одну кнопку:

![LLM_Studio_LLAMA3_Download](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LamaDownload.png)

Після завантаження LLM тиснемом кнопку `Local Server`(1) - запускаємо сервер(2) вибравши зі списку `Llama 3 - 8B Instruct`(3).

![LLM_Studio_LocalServerRun](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LocalServerRun.png)

Тепер можете написати боту, щоб протестувати його.

# Структура проєкту

Проєкт складається з декількох модулів, кожен з яких розділяє окремий функціонал, це зроблено для зручності обслуговування коду в майбутньому. Проєкт має наступну структуру:

- ui.py - Модуль графічного інтерфейсу(GUI) для конфігурування та запуску чат-боту.
- main.py - Головний модуль, котрий ініціалізує Telegram бота та всі інші модулі. Для запуску бота виконайте цей файл командою `python main.py` або `python3 main.py`.
- config.py - Модуль який містить конфігурації для чат боту, такі як API-ключ, шлях до каталогу з історією, температура віповідей, кількість токенів для відповіді та інше. 
- command_handler.py - Модуль обробки користувацьких команд, таких як увімкнення та вимкнення голосового режиму(аудіоповідомлень), старт нової бесіди(очищення файлу з історією), команда перекладу ботом тексту з англійської на українську мову.
- error_handling.py - Модуль у якому відбувається логування помилок.
- history_handler.py - Модуль, для роботи(завантаження та збереження) користувацької переписки, іншими словами історії чату. Використовується ID користувача Telegram для розділення розмов користувачів. Тобто один користувач - окрема історія спілкування. Переписка зберігається за наступним каталогом `conversations/id_Telegram_користувача/` у файл `current_history.json`.
- message_handler.py - Модуль, обробки повідомлень від великої мовної моделі. Використовується бібліотека від OpenAI
- voice_generator.py - Модуль, у якому відбувається генерація тексту(відповіді від LLM) у мовлення(TTS) українською мовою. Також там для конвертації OGG у WAV використовується бібліотека pydub https://pypi.org/project/pydub/
- voice_recognition.py - Модуль, де виконуються функції розпізнавання мовлення(з аудіо в текст), українською мовою, для подальної передачі тексту у велику мовну модель, яка у свою чергу генеруватиме відповідь користувачеві.


  ![ProjectStructurePicture](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/ProjectStructure.png)

  # Подяки

  Спасибі ChatGPT за асистування розробки проєкту.
