import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

def read_config(config_file):
    config = {}
    if os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as file:
            for line in file:
                if '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip().strip('"\'')
    return config

def save_config(config_file, config):
    # with open(config_file, 'w', encoding='utf-8') as file:
    #     for key, value in config.items():
    #         file.write(f'{key} = "{value}"\n')
    pass

def select_config_file():
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Виберіть файл config.py", filetypes=(("Python files", "config.py"), ("All files", "*.*")))
    if file_path:
        config_file_entry.delete(0, tk.END)
        config_file_entry.insert(0, file_path)
        config = read_config(file_path)
        fill_entries(config)

def fill_entries(config):
    bot_token_entry.delete(0, tk.END)
    bot_token_entry.insert(0, config.get('BOT_TOKEN', ''))

    openai_api_base_entry.delete(0, tk.END)
    openai_api_base_entry.insert(0, config.get('OPENAI_API_BASE', ''))

    openai_api_key_entry.delete(0, tk.END)
    openai_api_key_entry.insert(0, config.get('OPENAI_API_KEY', ''))

    llm_model_entry.delete(0, tk.END)
    llm_model_entry.insert(0, config.get('LLM_MODEL', ''))

    max_tokens_entry.delete(0, tk.END)
    max_tokens_entry.insert(0, config.get('MAX_TOKENS', ''))

    history_dir_entry.delete(0, tk.END)
    history_dir_entry.insert(0, config.get('HISTORY_DIR', ''))

def on_save():
    config_file = config_file_entry.get()
    if not os.path.exists(config_file):
        messagebox.showerror("Помилка", f"Файл {config_file} не існує")
        return

    config = read_config(config_file)
    config['BOT_TOKEN'] = bot_token_entry.get()
    config['OPENAI_API_BASE'] = openai_api_base_entry.get()
    config['OPENAI_API_KEY'] = openai_api_key_entry.get()
    config['LLM_MODEL'] = llm_model_entry.get()
    config['MAX_TOKENS'] = max_tokens_entry.get()
    config['HISTORY_DIR'] = os.path.join(history_dir_entry.get(), "conversation_histories")

    save_config(config_file, config)
    messagebox.showinfo("Збережено", "Конфігурацію збережено успішно")

# Створення основного вікна
root = tk.Tk()
root.title("Конфігурація бота")

# Вибір файлу config.py
tk.Label(root, text="Файл config.py:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
config_file_entry = tk.Entry(root, width=50)
config_file_entry.grid(row=0, column=1, padx=10, pady=5)
config_file_entry.insert(0, "Виберіть шлях до config.py")
config_file_button = tk.Button(root, text="Вибрати файл", command=select_config_file)
config_file_button.grid(row=0, column=2, padx=5)

# Параметри конфігурації
tk.Label(root, text="BOT_TOKEN").grid(row=1, column=0, padx=10, pady=5, sticky="e")
bot_token_entry = tk.Entry(root, width=50)
bot_token_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="OPENAI_API_BASE").grid(row=2, column=0, padx=10, pady=5, sticky="e")
openai_api_base_entry = tk.Entry(root, width=50)
openai_api_base_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="OPENAI_API_KEY").grid(row=3, column=0, padx=10, pady=5, sticky="e")
openai_api_key_entry = tk.Entry(root, width=50)
openai_api_key_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="LLM_MODEL").grid(row=4, column=0, padx=10, pady=5, sticky="e")
llm_model_entry = tk.Entry(root, width=50)
llm_model_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="MAX_TOKENS").grid(row=5, column=0, padx=10, pady=5, sticky="e")
max_tokens_entry = tk.Entry(root, width=50)
max_tokens_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="HISTORY_DIR").grid(row=6, column=0, padx=10, pady=5, sticky="e")
history_dir_entry = tk.Entry(root, width=50)
history_dir_entry.grid(row=6, column=1, padx=10, pady=5)

# Кнопка збереження
save_button = tk.Button(root, text="Зберегти", command=on_save)
save_button.grid(row=7, column=0, columnspan=2, pady=10)

# Заповнення полів з config.py
fill_entries(read_config(config_file_entry.get()))

# Запуск головного циклу
root.mainloop()
