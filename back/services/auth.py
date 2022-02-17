from back.services.base import BaseService

from back.common import discord
from back.crud.users import UsersCRUD
from back.schemas.auth import OAuth2Code

class AuthService(BaseService):
    async def auth_discord(self, oauth_form: OAuth2Code) -> str:
        """Создание или обновление пользователя, возвращение user_id

        Args:
            oauth_form (OAuth2Code): JSON форма, содержащая код
        """

        code =  oauth_form.code
        access_token = await discord.get_discord_token(code)
        profile_in = await discord.get_discord_profile(access_token)

        user_id = await UsersCRUD.create_or_update(self.db_session, profile_in)
        
        return user_id