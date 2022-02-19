import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv(".env")

DEBUG = True
TITLE = "Prohojemba"
VERSION = "0.0.6"
LOGS_FILE_PATH = "server.logs"
DOMAIN = "127.0.0.1"

# Безопасность
SECRET_KEY = os.environ.get("SECRET_KEY")
ACCESS_TOKEN_LIFETIME = timedelta(hours=6)

# Подключение к БД
DATABASE_URI = os.environ.get("DATABASE_URI")

# Подключение к Redis
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_PASSWORD = ""

REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}?password={REDIS_PASSWORD}"


# Discord OAuth2
DISCORD_CLIENT_ID = os.environ.get("DISCORD_CLIENT_ID")
DISCORD_SECRET_KEY = os.environ.get("DISCORD_SECRET_KEY")

DISCORD_REDIRECT_URL = "http://localhost:8000/auth"