from fastapi import FastAPI

from back.core import config
from back.api.v1.api import v1_router


async def _on_startup():
    # await database.connect()
    pass

async def _on_shutdown():
    # await database.disconnect()
    pass

# Инициализация экземпляра приложения
app = FastAPI(
    title=config.TITLE,
    version=config.VERSION,
    on_startup=[
        _on_startup
    ],
    on_shutdown=[
        _on_shutdown
    ]
)

app.include_router(v1_router, prefix="/api/v1")



