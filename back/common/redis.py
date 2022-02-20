import aioredis

from back.core import config


redis_cache = aioredis.from_url(config.REDIS_URL, db=1, encoding="utf-8")

