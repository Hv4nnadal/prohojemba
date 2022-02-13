# Настройка логирования
import logging

from .. import settings

logger = logging.getLogger(settings.TITLE)
logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
handler = logging.FileHandler(settings.LOGS_FILE_PATH, mode="a", encoding="utf-8")
formatter = logging.Formatter(
    "%(levelname)s: %(asctime)s (file: %(filename)s, line: %(lineno)d, func: %(funcName)s) - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
