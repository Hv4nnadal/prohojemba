from fastapi import FastAPI
import uvicorn
import logging

from . import settings
from .db.base import database
from .routes import routes

logging.basicConfig(
    filename="server.logs",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)


async def _on_startup():
    await database.connect()


async def _on_shutdown():
    await database.disconnect()

# Инициализация экземпляра приложения
app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    on_startup=[
        _on_startup
    ],
    on_shutdown=[
        _on_shutdown
    ]
)

# Подлключение обработчиков
for path, router in routes.items():
    app.include_router(router, prefix=path)

if __name__ == "__main__":
    uvicorn.run(app)

