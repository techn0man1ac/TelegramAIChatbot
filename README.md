# Ukrainian Telegram Chatbot with AI

![Copilot_Generated_Bot_Image](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/CopilotGeneratedBotImage.jpg)

This project aims to develop a Ukrainian chatbot using the ChatGPT language model. The project is authored by Serhii Trush.

# Key Features

![Voice_conversations_mode](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/conversationVoice.png)

Ukrainian Language: The chatbot is capable of understanding and generating text in Ukrainian.
Speech Recognition and Generation: The chatbot can recognize and generate speech in Ukrainian.
Telegram Messenger: The chatbot operates within the Telegram messenger platform.
Conversation Context: The chatbot maintains conversation context to provide more coherent responses.

# Project Structure

The project consists of the following files:
- config.py: Configuration file containing parameters such as API keys and file paths.
- command_handler.py: Module for handling user commands and managing conversation states.
- error_handling.py: Module for logging errors that occur during the execution of the program.
- history_handler.py: Module for managing conversation history, including loading and saving.
- main.py: Main entry point of the program, responsible for starting the bot and handling messages.
- message_handler.py: Module for processing user messages and generating responses using the ChatGPT model.
- voice_generator.py: Module for generating speech output based on text input.
- voice_recognition.py: Module for recognizing speech input and converting it to text.
- ui.py: User interface module for configuring the bot settings.

  ![User_interface](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/UIConfigurationBot.png)

# Usage

To use the chatbot, deploy the project on a server and set up a Telegram bot using the provided token. Users can interact with the bot by sending text or voice messages in Ukrainian. The bot will respond accordingly based on the conversation context and user input.

![Commands_conversation](https://raw.githubusercontent.com/techn0man1ac/TelegramAIChatbot/main/imgs/conversationCommands.png)

# Acknowledgments

Thanks to ChatGPT for their help with the project.

# License

This project is licensed under the MIT License - see the LICENSE file for details.
