import os
import logging
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv(".env")

DEBUG = True
TITLE = "Prohojemba"
VERSION = "0.0.6"
DOMAIN = "127.0.0.1"

LOGGING_CONFIG = {
    "filename": "server.logs",
    "filemode": "w",
    "level": logging.DEBUG if DEBUG else logging.INFO,
    "format": "%(levelname)s: %(asctime)s (file: %(filename)s, line: %(lineno)d, func: %(funcName)s) - %(message)s"
}

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

# Токен бота, отправляющиего уведомления о критических ошибках
DISCORD_BOT_LOGGER = os.environ.get("DISCORD_BOT_TOKEN")
DISCORD_LOG_CHANNEL_ID = os.environ.get("DISCORD_LOG_CHANNEL")