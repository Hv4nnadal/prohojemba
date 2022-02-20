from distutils import errors
from aiohttp import ClientSession, ClientConnectionError

from back.core import config
from back.exceptions.discord import DiscordGetAccessTokenException, DiscordGetUserProfileException
from back.schemas.users import UserIn


async def get_discord_token(code: int) -> str:
    async with ClientSession() as session:
        try:
            async with session.post(
                url="https://discord.com/api/oauth2/token",
                data={
                    'client_id': config.DISCORD_CLIENT_ID,
                    'client_secret': config.DISCORD_SECRET_KEY,
                    'grant_type': 'authorization_code',
                    'code': code,
                    'redirect_uri': config.DISCORD_REDIRECT_URL
                },
                headers={
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            ) as resp:
                resp_data: dict = await resp.json()
                if not resp.status == 200:
                    raise DiscordGetAccessTokenException(f"CODE={resp.status} DETAIL={resp_data.get('error_description')}")

            return resp_data.get("access_token")
        
        # На случай если сервер Discord не отвечает
        except ClientConnectionError:
            raise DiscordGetAccessTokenException("CODE=501 DETAIL=Connection to server error")


async def get_discord_profile(token: str) -> UserIn:
    async with ClientSession() as session:
        async with session.get(
            url="https://discord.com/api/users/@me",
            headers={
                "Authorization": f"Bearer {token}"
            }
        ) as resp:
            resp_data: dict = await resp.json()
            if not resp.status == 200:
                raise DiscordGetUserProfileException(resp_data.get("error_description"))

    return UserIn.parse_obj(resp_data)


async def send_error_info_to_channel(err: Exception) -> None:
    """Отправка уведомления на указанный канал в дискорд
    """
    async with ClientSession() as session:
        async with session.post(
            url=f"https://discord.com/api/channels/{config.DISCORD_LOG_CHANNEL_ID}/messages",
            headers={
                "Authorization": f"Bot {config.DISCORD_BOT_LOGGER}"
            },
            data={
                "content": f"Критическая ошибка на сервере: {type(err)}"
            }
        ) as resp:
            pass

