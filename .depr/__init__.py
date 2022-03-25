import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from back.core import config
from back.common import discord
from back.api.v1.api import v1_router


async def _on_startup():
    # Всякие инициализации при запуске сервера
    logging.basicConfig(**config.LOGGING_CONFIG)


async def _on_shutdown():
    from back.common.redis import redis_cache
    from back.common.db import Session
    Session.close_all()
    await redis_cache.close()



# Инициализация экземпляра приложения
app = FastAPI(
    title=config.TITLE,
    version=config.VERSION,
    on_startup=[_on_startup],
    on_shutdown=[_on_shutdown]
)

app.include_router(v1_router, prefix="/api/v1")

@app.exception_handler(500)
async def handle_crytical_server_error(request, exc) -> JSONResponse:
    await discord.send_error_info_to_channel(exc)
    return JSONResponse({"detail": "Internal Server Error"}, 500)

