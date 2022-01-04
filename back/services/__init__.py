from aioredis import Redis

from .auth import AuthService
from .cache import CacheService
from .email import EmailService

from back import settings

redis_service = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
auth_service = AuthService(settings.SECRET_KEY, redis_service)
email_service = EmailService(settings.MAIL_CONFIG)
