import os
from dotenv import load_dotenv
load_dotenv(".env")

DEBUG = True
TITLE = "Prohojemba"
VERSION = "0.0.5"
LOGS_FILE_PATH = "server.logs"

# Безопасность
SECRET_KEY = os.environ.get("SECRET_KEY")

# Подключение к БД
DATABASE_URI = os.environ.get("DATABASE_URI")

# Подключение к Redis


# Discord OAuth2
DISCORD_CLIENT_ID = os.environ.get("DISCORD_CLIENT_ID")
DISCORD_SECRET_KEY = os.environ.get("DISCORD_SECRET_KEY")

DISCORD_REDIRECT_URL = "http://localhost:8000/auth"