from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from back.api import deps
from back.core import security
from back.common.log import logger
from back.exceptions.discord import DiscordGetAccessTokenException, DiscordGetUserProfileException, DiscordServerNotResponse
from back.schemas.auth import OAuth2Code, TokensPair
from back.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Авторизация"])


@router.post("/discord", response_model=TokensPair)
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
        user_id: int = await auth_service.create_or_update_profile_from_discord(oauth_form)
        new_tokens_pair: TokensPair = await security.generate_tokens_pair(user_id) 
        
        # Инициализация ответа и создание печенек
        resp = JSONResponse(content=new_tokens_pair.dict())
        resp.set_cookie("refresh_token", new_tokens_pair.refresh_token, domain="127.0.0.1", httponly=True, max_age=604800)
        return resp

    # Обработка ошибок Discord
    except (DiscordGetAccessTokenException, DiscordGetUserProfileException, DiscordServerNotResponse) as e:
        logger.error(f"{e}: {e.detail}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.detail
        )   


@router.post("/token")
async def update_token(
    user_id: int = Depends(deps.get_user_id_by_refresh_token)
):
    """
    Обновление токенов при помощи refresh токена
    """
    new_tokens_pair: TokensPair = await security.generate_tokens_pair(user_id)
    resp = JSONResponse(content=new_tokens_pair.dict())
    resp.set_cookie("refresh_token", new_tokens_pair.refresh_token, domain="127.0.0.1", httponly=True, max_age=604800)
    return resp