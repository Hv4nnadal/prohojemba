from typing import Optional
import aioredis


class CacheService:
    def __init__(self, host: str, port: int):
        self.redis_connection = aioredis.Redis(
            host=host,
            port=port
        )

    async def set_activation_code(self, code: str, user_id: int) -> None:
        await self.redis_connection.set(f"activate:{code}", user_id)

    async def get_user_id_by_code(self, code: str) -> Optional[int]:
        return await self.redis_connection.get(f"activate:{code}")
