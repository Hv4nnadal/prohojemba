from os import environ

# Базовая информация о приложении
DEBUG = True
if DEBUG:
    from dotenv import load_dotenv
    load_dotenv(".env")

TITLE = "Prohojemba"
VERSION = "0.0.1"

LOGS_FILE_PATH = "server.logs"

# Безопасность
SECRET_KEY = environ.get("SECRET_KEY")

# Настройки подключения к базе денных(По умолчанию тестовая БД)
DATABASE_URI = environ.get("DATABASE_URI")
print(DATABASE_URI)

# Настройка подключения к почтовому сервису
MAIL_CONFIG = {
    "MAIL_USERNAME": "ezzik98",
    "MAIL_PASSWORD": "kexfrbokgmtbufgl",
    "MAIL_FROM": "ezzik98@yandex.ru",
    "MAIL_SERVER": "smtp.yandex.ru",
    "MAIL_PORT": 465,
    "MAIL_FROM_NAME": "Prohojemba",
    "MAIL_TLS": False,
    "MAIL_SSL": True,
    "USE_CREDENTIALS": True,
    "VALIDATE_CERTS": True
}

# Настройка подключения к Redis
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379

# Настройки сервиса сохранения изображений
# Внешний сервис
IMGBB_TOKEN = None  # Токен для работы с https://imgbb.com

# Локальные настройки
IMAGES_DIR = "D:\\github.com\\prohojemba\\images"  # Директория для сохранения изображений

WALK_STATUSES = (
    "not_played",  # Пользователь даже не прикасался к продукту
    "in_progress",  # Пользователь в процессе прохождения\просмотра
    "completed",  # Пользователь закончил просмотр/прохождение
    "full_completed"  # (Скорее всего ставится только для игр) Прохождение со всеми ачивками
)

TITLE_TYPES = ("game", "anime", "film", "series")
