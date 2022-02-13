from back.services.base import BaseService

from back.schemas.auth import OAuth2Code

class AuthService(BaseService):
    async def auth_discord(oauth_form: OAuth2Code):
        """Создание или обновление пользователя

        Args:
            oauth_form (OAuth2Code): JSON форма, содержащая код
        """
        code =  oauth_form.code
