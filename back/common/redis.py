import aioredis

from back.core import config


class RedisConnection:
    async def __aenter__(self) -> aioredis.Redis:
        self.conn = aioredis.from_url(config.REDIS_URL, db=1, encoding="utf-8")
        return self.conn

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.conn.close()

