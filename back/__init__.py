from fastapi import FastAPI

from . import settings
from .routes import routes

# Инициализация экземпляра приложения
app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION
)
# Подлключение обработчиков
for path, router in routes.items():
    app.include_router(router, prefix=path)

