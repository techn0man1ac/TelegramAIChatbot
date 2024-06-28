[![UA_version_README](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/Flags/UA%402x.png)](https://github.com/techn0man1ac/TelegramAIChatbot/)
[![GB_version_README](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/Flags/GB%402x.png)](https://github.com/techn0man1ac/TelegramAIChatbot/blob/main/README_EN.md)

# Ukrainian-language Telegram chatbot with AI

![Copilot_Generated_Bot_Image](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/CopilotGeneratedBotImage.jpg)
> The project wrapper was generated using Copilot in Windows, the original wrapper image can be found [here](https://www.bing.com/images/create/tech01aibot-telegram-bot-image-with-the-text-27hell/1-66376f0c15b14dce9b8543e76374b77a?id=%2ffnQhXHy14ZA7U%2bG1mpTTg%3d%3d&view=detailv2&idpp=genimg&idpclose=1&thId=OIG2.0xK8wnUzR5ppwvD_Vfi3&frame=sydedg&FORM=SYDBIC).

Ukrainian-language Telegram chatbot using artificial intelligence. This project is based on LLM Studio, which works as a server for the large language model LLAMA3 8B from META. It processes user messages and generates chatbot tokens (responses).

# Features.

This chatbot can generate both text and audio messages in Ukrainian. Speech synthesis and recognition are implemented using Python libraries from Google:
- SpeechRecognition: https://pypi.org/project/SpeechRecognition/
- gTTS (Google Text-to-Speech): https://pypi.org/project/gTTS/

I used Telegram messenger as an interface for interacting with artificial intelligence, which is convenient because you can access your own AI from your smartphone anywhere with an Internet connection. 

![Voice_conversations_mode](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/conversationVoice.png)

Here is a link to the Telegram API: https://core.telegram.org/bots/api

To work with the Telegram API, use the pyTelegramBotAPI library: https://pypi.org/project/pyTelegramBotAPI/

The context of the conversation, namely the contents of the `history` variable in the `message_handler.py` file (correspondence with the chat bot) is saved in JSON format (directory `conversations/id_Telegram_user/current_history.json`) to disk, so that even after reloading the script, the bot "remembers" what you talked to it earlier.

![Context](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/context.png)

A standard library is used to implement reading the JSON structure: https://docs.python.org/uk/3/library/json.html

To work with a large language model, 2 software elements are used, namely the library from OpenAI, which in turn interacts with LLM Studio.
- You can work with the OpenAI API in Python using the library, here is the link: https://pypi.org/project/openai/
This library has a wide range of functionality for working with AI, and I chose it for my chatbot project because of this convenience. Although it is designed to work with OpenAI products, it can also be used for other projects, such as LLM Studio.
- LLM Studio is a handy tool with a graphical user interface (GUI), it is useful for getting started with large language models (LLM), you can download it for your operating system here: https://lmstudio.ai/

![LLM_Studio](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LLM_Studio.png)

# Library versions at the time of development

This project uses several key libraries, here they are:

- telebot == 0.0.5
- openai == 1.33.0
- gTTS == 2.5.1
- SpeechRecognition == 3.10.4
- pydub == 0.25.1

# Installing and configuring the software

Install Python https://www.python.org/downloads/

Then for the library(except for the library itself) pydub to work, you need to install FFmpeg, here's how to install it: https://www.editframe.com/guides/how-to-install-and-start-using-ffmpeg-in-under-10-minutes

After installing LLM Studio, you need to download LLM, for my project, I used LLAMA3 with 8 billion parameters (8B) from META: https://llama.meta.com/llama3/

To install a large language model in your system, you need to download it to LLM Studio, for this we take the following steps:

![LLM_Studio_LLAMA3_Download](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LLM_Studio_LLAMA3_Download.png)

1. Click the search button.
2. Write the name of the desired LLM in the search field, in my case it is `Llama 3 8B Instruct`.
3. Download it. There are different versions of quantization (compression of information stored in the LLM), I suggest starting with `Q4_K_M` - the golden mean between speed and quality of answers. For more productive computers there are "Q8" or "fp32" versions.

After loading the large language model, click the `Local Server` button to start the server, which will provide the ability to "communicate" with LLM using the local server at `http://localhost:1234/v1` or `http://localhost:1234/v1/chat/completions`.

![LLM_Studio_LocalServerStart](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LLM_Studio_LocalServerStart.png)

After setting up the software, you need to get an API key, here's a great article on how to do it: https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/

![TelegramBotFather](https://github.com/techn0man1ac/TelegramAIChatbot/blob/main/imgs/TelegramBotFather.png)

The next step is to register the API key received from `@botfather` in the code of the file `config.py` or for convenience, you can enter all the parameters by running the script `ui.py`.

![BotConfigUserInterface](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/BotConfigUserInterface.png)

1. Open the file `config.py` thereby setting the absolute address to the working directory with the project.
2. Copy the API key (change the keyboard layout to "eng", this is important). And it is also important to copy the absolute path to the `conversations` directory in the `HISTORY_DIR` field, for example `C:\Projects\TelegramAIChatbot\conversations\`.
3. Save the configuration to the `config.py` file by clicking the button.
4. Launch the bot from the button and not by executing the main script. After that, the Telegram chatbot will execute the `main.py` file and everything should work - you can write your chatbot in Ukrainian.

# Project structure

The project consists of several modules, each of which has its own functionality, this is done for the convenience of maintaining the code in the future. The project has the following structure:

- ui.py - Graphical User Interface (GUI) module for configuring and launching the chatbot.
- main.py - The main module that initializes the Telegram bot and all other modules. To run the bot, execute this file with the command `python main.py` or `python3 main.py`.
- config.py - A module that contains the configurations for the chatbot, such as the API key, path to the history directory, message temperature, number of tokens to respond, etc. 
- command_handler.py - A module for processing user commands, such as enabling and disabling voice mode (audio messages), starting a new conversation (clearing the history file), and a command to translate text from English into Ukrainian.
- error_handling.py - The module in which errors are logged.
- history_handler.py - A module for working (downloading and saving) user correspondence, in other words, chat history. Telegram user ID is used to separate user conversations. That is, one user has a separate communication history. The correspondence is stored in the following directory `conversations/id_Telegram_user/` in the file `current_history.json`.
- message_handler.py - A module that processes messages from a large language model. The library from OpenAI is used.
- voice_generator.py - A module that generates text (response from LLM) into speech (TTS) in Ukrainian. Also, to convert OGG to WAV, it uses the pydub library https://pypi.org/project/pydub/
- voice_recognition.py - A module that performs speech recognition functions (from audio to text) in Ukrainian for further transfer of the text to a large language model, which in turn will generate a response to the user.

![ProjectStructurePicture](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/ProjectStructure.png)

# Acknowledgments

We would like to thank ChatGPT for assisting with the development of the project.
