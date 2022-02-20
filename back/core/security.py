import jwt
from fastapi.security import HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta

from back.schemas.auth import TokensPair
from back.core import config
from back.common.redis import redis_cache


hasher = CryptContext(schemes=["bcrypt"])
bearer = HTTPBearer(auto_error=False)


def _generate_access_token(user_id: int, expires_at: int) -> str:
    """Генерация access токена, содаржащего id пользователя, дату истечения и тип токена"""
    return jwt.encode(
        payload={
            "user_id": user_id,
            "exp": expires_at,
            "type": "access_token"
        }, key=config.SECRET_KEY
    )


def validate_access_token(token: str) -> int:
    """Расшифровка access токена, его валидация и получение id пользователя
    """
    payload = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
    if user_id := payload.get("user_Id"):
        return user_id
    raise jwt.InvalidTokenError


async def _generate_refresh_token(user_id: int) -> str:
    """Генерация access токена, содаржащего id пользователя, дату истечения и тип токена"""
    token = jwt.encode(
        payload={
            "user_id": user_id,
            "type": "refresh_token"
        }, key=config.SECRET_KEY
    )
    await redis_cache.set(str(user_id), token)

    return token


async def validate_refresh_token(token: str) -> int:
    payload = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
    user_id = payload.get("user_id")
    
    saved_token = await redis_cache.get(user_id)
    if saved_token == token:
        return user_id
    
    raise jwt.InvalidTokenError
    
        
async def generate_tokens_pair(user_id: int) -> TokensPair:
    """Генерация новой пары токенов
    """
    # Получение времени истечения токена UNIX TIMESTAMP
    expires_at = int((
        datetime.now()+config.ACCESS_TOKEN_LIFETIME
    ).timestamp())

    return TokensPair(
        expires_at=expires_at,
        access_token=_generate_access_token(user_id, expires_at),
        refresh_token= await _generate_refresh_token(user_id)
    )

