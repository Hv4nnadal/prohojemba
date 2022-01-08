from aioredis import Redis

from .auth import AuthService
from .email import EmailService
from .images.local import LocalImage
from .images.imagebb import ImageBB

from back import settings

redis_service = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
auth_service = AuthService(settings.SECRET_KEY, redis_service)
email_service = EmailService(settings.MAIL_CONFIG)

image_service = ImageBB(settings.IMGBB_TOKEN) if settings.IMGBB_TOKEN \
    else LocalImage(settings.IMAGES_DIR)
