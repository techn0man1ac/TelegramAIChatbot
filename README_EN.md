[![UA_version_README](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/Flags/UA%402x.png)](https://github.com/techn0man1ac/TelegramAIChatbot/)
[![GB_version_README](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/Flags/GB%402x.png)](https://github.com/techn0man1ac/TelegramAIChatbot/blob/main/README_EN.md)

# Ukrainian-language Telegram chatbot with AI

![Copilot_Generated_Bot_Image](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/CopilotGeneratedBotImage.jpg)
> The project wrapper was generated using Copilot in Windows, the original wrapper image can be found [here](https://www.bing.com/images/create/tech01aibot-telegram-bot-image-with-the-text-27hell/1-66376f0c15b14dce9b8543e76374b77a?id=%2ffnQhXHy14ZA7U%2bG1mpTTg%3d%3d&view=detailv2&idpp=genimg&idpclose=1&thId=OIG2.0xK8wnUzR5ppwvD_Vfi3&frame=sydedg&FORM=SYDBIC).

Ukrainian-language Telegram chatbot using artificial intelligence. This project is based on LM Studio, which works as a server for the large language model LLAMA3 8B from META. It processes user messages and generates chatbot tokens (responses).

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

To work with a large language model, 2 software elements are used, namely the library from OpenAI, which in turn interacts with LM Studio.
- You can work with the OpenAI API in Python using the library, here is the link: https://pypi.org/project/openai/
This library has a wide range of functionality for working with AI, and I chose it for my chatbot project because of this convenience. Although it is designed to work with OpenAI products, it can also be used for other projects, such as LM Studio.
- LM Studio is a handy tool with a graphical user interface (GUI), it is useful for getting started with large language models (LLM), you can download it for your operating system here: https://lmstudio.ai/

![LLM_Studio](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LLM_Studio.png)

# Library versions at the time of development

This project uses several key libraries, here they are:

- telebot == 0.0.5
- openai == 1.33.0
- gTTS == 2.5.1
- SpeechRecognition == 3.10.4
- pydub == 0.25.1

# Install and configure the software

First, install Python https://www.python.org/downloads/

Next, install Git https://git-scm.com/downloads and log in using GitHub.

Download the repository to the directory you need (for example, "C:\Projects\") using the "git clone" command, which we write in the command line (CMD):

`git clone https://github.com/techn0man1ac/TelegramAIChatbot.git`.

You can also download without git, that is, without registration, simply by downloading the repository archive from this link: https://github.com/techn0man1ac/TelegramAIChatbot/archive/refs/heads/main.zip

After downloading, go to the "TelegramAIChatbot" directory, then write in the command line `cd TelegramAIChatbot` - move to the directory with the project files;

Install all the necessary libraries for the chatbot to work (see the screenshot below):

`pip install -r requirements.txt`.

![RequirementsInstall](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/CMD.png)

It may be the case (but not necessarily) that for the pydub library to work (in addition to the library itself), you need to install FFmpeg, here's how to install it: https://www.editframe.com/guides/how-to-install-and-start-using-ffmpeg-in-under-10-minutes

After installing the libraries, go to the "code" directory with the command `cd code` and run the bot's GUI module with the command `python UI.py`:

![RunUI](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/CMD_RUN.png)

The graphical interface with the chatbot configuration will open:

![BotConfigUserInterface](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/BotConfigUserInterface.png)

At this stage, you need to take the following steps:

1) Select the path to the configuration file "config.py" using the button on the top right;
2) When the parameters are loaded (all fields are filled in), you need to get the API key from the main Telegram bot. It can be found by typing @BotFather( https://t.me/BotFather ) in the contact search field in Telegram. The interface is intuitive, you create a bot by naming it, then go to the bot management and click the button to get the API key. Just in case, I'll leave you this link https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/, which describes how to get it first (to the Python code).
Important note - before changing the "BOT_TOKEN" field, change the keyboard layout to English, and then insert the key.
3) Then click "Save configuration".
4) Click the "Run bot" button and in the console that runs with the UI.py module, a message will appear that the bot is in the runtime (I sent him 2 messages, which can be seen in the logs):

![BotRun](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/BotRun.png)

After installing LM Studio, you need to download LLM, for my project, as an AI, I used LLAMA3 with 8 billion parameters (8B) from META: https://llama.meta.com/llama3/

To install a large language model in your system, you need to download it to LM Studio, for this we just click one button:

![LLM_Studio_LLAMA3_Download](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LamaDownload.png)

After loading the large language model, press the `Local Server` button (1) - start the server (2) by selecting `Llama 3 - 8B Instruct`(3).

![LLM_Studio_LocalServerRun](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/LocalServerRun.png)

Now you can write to the bot in Telegram to test the work.

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
