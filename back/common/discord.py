from aiohttp import ClientSession

from back.core import config
from back.exceptions.discord import DiscordGetAccessTokenException, DiscordGetUserProfileException
from back.schemas.users import UserIn


async def get_discord_token(code: int) -> str:
    async with ClientSession() as session:
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
                raise DiscordGetAccessTokenException(resp_data.get("error_description"))

    return resp_data.get("access_token")


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