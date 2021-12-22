from .auth import AuthService

from back import settings

auth_service = AuthService(settings.SECRET_KEY)