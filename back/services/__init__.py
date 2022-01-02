from .auth import AuthService
from .cache import CacheService
from .email import EmailService

from back import settings

auth_service = AuthService(settings.SECRET_KEY)
cache_service = CacheService(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
email_service = EmailService(settings.MAIL_CONFIG)
