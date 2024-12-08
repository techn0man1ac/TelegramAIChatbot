'''
Ukrainian-language Telegram chatbot using artificial intelligence. 
This project is based on LM Studio, which works as a server for the large language model LLAMA3 8B from META. 
It processes user messages and generates chatbot tokens (responses).

https://github.com/techn0man1ac/TelegramAIChatbot

By Serhii Trush, 2024, MIT License.
'''

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess 
from error_handling import log_error

config_file_path = ''

# Function to select the config.py file
def select_config_file():
    global config_file_path
    # Prompt user to choose a config.py file with an initial directory of the current working folder
    config_file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Виберіть файл config.py", filetypes=(("Python files", "config.py"), ("All files", "*.*")))
    if config_file_path:
        # Clear the text field and insert the path to the selected file
        config_file_entry.delete(0, tk.END)
        config_file_entry.insert(0, config_file_path)
        # Read the configuration file and fill input fields
        config_dict = read_config_file(config_file_path)
        fill_entries(config_dict)

# Function to fill input fields with values from the configuration file
def fill_entries(config_dict):
    for key, value in config_dict.items():
        entry = entry_widgets.get(key)
        if entry:
            entry.delete(0, tk.END)
            entry.insert(0, value)

# Function to save the bot configuration
def on_save():
    if config_file_path == '':
        messagebox.showerror("Помилка", "Виберіть файл config.py")
        return

    config_dict = {}
    for key, entry in entry_widgets.items():
        config_dict[key] = entry.get()

    save_config(config_file_path, config_dict)
    messagebox.showinfo("Збережено", "Конфігурацію бота збережено успішно")

# Function to read the configuration file
def read_config_file(config_file):
    config = {}
    if os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as file:
            for line in file:
                # Split key and value by the '=' character
                if '=' in line:
                    key, value = line.split('=') # Example, input - "BOT_WRITE_TIMEOUT='480'\n", output - key = 'BOT_WRITE_TIMEOUT', value = "'480'\n"
                    if key == 'HISTORY_DIR': # Change history catalog
                        value = f"{os.path.dirname(config_file)}/conversations/" # add for path catalog "conversations" 
                    config[key] = value.strip('\'\n') # Example output - 'OPENAI_API_BASE': 'http://localhost:1234/v1/'
    return config

# Function to save the configuration to a file
def save_config(config_file, config):
    with open(config_file, 'w', encoding='utf-8') as file:
        for key, value in config.items():
            file.write(f"{key}=\'{value}\'\n")

# Function to start the bot
def start_bot():
    try:
        # try python or python3
        subprocess.Popen(["python", "main.py"], cwd=os.path.dirname(__file__)) 

    except Exception as e:
        error_message = "Помилка", f"Помилка запуску бота: {e}"   
        log_error(error_message)
        messagebox.showerror(error_message)

# Create the main application window
root = tk.Tk()
root.title("TelegramAIChatbot конфігурація")

# Elements to select and enter the path to the configuration file
tk.Label(root, text="Файл config.py:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
config_file_entry = tk.Entry(root, width=50)
config_file_entry.grid(row=0, column=1, padx=10, pady=5)
config_file_entry.insert(0, "Виберіть шлях до config.py")
config_file_button = tk.Button(root, text="Вибрати файл", command=select_config_file)
config_file_button.grid(row=0, column=2, padx=5)

# List of bot configuration parameters
parameters = [
    "BOT_TOKEN",
    "OPENAI_API_BASE",
    "OPENAI_API_KEY",
    "LLM_MODEL",
    "MAX_TOKENS",
    "BOT_WRITE_TIMEOUT",
    "BOT_TEMPERATURE",
    "HISTORY_DIR"
]

# Dictionary to store input fields
entry_widgets = {}

# Create and place input elements for each parameter
for i, parameter in enumerate(parameters):
    tk.Label(root, text=parameter).grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root, width=50)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    entry_widgets[parameter] = entry

# Button to save the configuration
save_button = tk.Button(root, text="Зберегти конфігурацію", command=on_save)
save_button.grid(row=len(parameters)+1, column=0, columnspan=2, pady=10)

# Button to start the bot
start_bot_button = tk.Button(root, text="Запустити бот", command=start_bot)
start_bot_button.grid(row=len(parameters)+2, column=0, columnspan=2, pady=10)

# Start the main loop of the application
root.mainloop()
