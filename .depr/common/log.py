# Настройка логирования
import logging

from back.core import config

logger = logging.getLogger(config.TITLE)
logger.setLevel(logging.DEBUG if config.DEBUG else logging.INFO)
handler = logging.FileHandler(config.LOGS_FILE_PATH, mode="a", encoding="utf-8")
formatter = logging.Formatter(
    "%(levelname)s: %(asctime)s (file: %(filename)s, line: %(lineno)d, func: %(funcName)s) - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
