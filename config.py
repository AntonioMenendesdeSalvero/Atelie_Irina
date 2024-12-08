import os
from dotenv import load_dotenv

# Завантаження змінних з файлу .env
load_dotenv()

# Отримання значень
BOT_TOKEN = os.getenv("BOT_TOKENS")
DATABASE_PATH = os.getenv("DATABASE_PATH")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS").split(",")))
