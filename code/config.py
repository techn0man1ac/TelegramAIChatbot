'''
config.py
'''

import os

# Bot configuration
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# OpenAI configuration
OPENAI_API_BASE = "http://localhost:1234/v1"
OPENAI_API_KEY = "lm-studio"
LLM_MODEL = "MaziyarPanahi/Llama-3-8B-Instruct-DPO-v0.3-32k-GGUF"

MAX_TOKENS = 512 
# MAX TOKENS in one message
BOT_WRITE_TIMEOUT = 480 
# 480 sec = 8 minutes per message max
BOT_TEMPERATURE = 0.4 
# Higher more random answer

HISTORY_DIR = "MyProjects/AI/conversations/"
# History directory

if not os.path.exists(HISTORY_DIR):
    os.makedirs(HISTORY_DIR)
