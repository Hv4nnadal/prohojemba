from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from back.api import deps
from back.core import securiry
from back.common.log import logger
from back.exceptions.discord import DiscordGetAccessTokenException, DiscordGetUserProfileException
from back.schemas.auth import OAuth2Code, TokenData
from back.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Авторизация"])


@router.post("/discord", response_model=TokenData)
async def auth_from_discord( 
    oauth_form: OAuth2Code,
    db: AsyncSession = Depends(deps.get_db_connection)
):
    """
    Вход при помощи аккаунта Discord
    
    Ссылка для авторизации: https://discord.com/api/oauth2/authorize?client_id=887980562315370506&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fauth&response_type=code&scope=identify
    
    """
    auth_service = AuthService(db)
    try:
        user_id = await auth_service.auth_discord(oauth_form)
    except (DiscordGetAccessTokenException, DiscordGetUserProfileException) as e:
        logger.error(f"{e}: {e.detail}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.detail
        )
    # Генерация нового access токена
    access_token_data = securiry.generate_access_token(user_id)

    # Генерация refresh токена


@router.post("/token")
async def update_token(
    user_id: int = Depends(deps.get_user_id_by_refresh_token)
):
    """
    Обновление токенов при помощи refresh токена
    """
    pass