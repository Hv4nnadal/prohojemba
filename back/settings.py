from os import environ

# Базовая информация о приложении
TITLE = "Prohojemba"
VERSION = "0.0.1"

SECRET_KEY = environ.get("SECRET_KEY", "debug-secret-key")

# Настройки подключения к базе денных
DATABASE_URI = environ.get("DATABASE_URI", "sqlite:///debug.db")

# Настройка подключения к почтовому сервису


# Настройка подключения к Redis


# Настройка сервиса сохранения изображений
IMGBB_TOKEN = None # Токен для работы с https://imgbb.com
IMAGES_DIR = "D:\\images" # Директория для сохранения изображений

WALK_STATUSES = (
    "not_played",       # Пользователь даже не прикасался к продукту
    "in_progress",      # Пользователь в процессе прохождения\просмотра 
    "completed",        # Пользователь закончил просмотр/прохождение
    "full_completed"    # (Скорее всего ставится только для игр) Прохождение со всеми ачивками
)

TITLE_TYPES = ("game", "anime", "film", "series")
