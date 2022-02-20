import jwt
from typing import Generator
from fastapi import Cookie, Security, status
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException

from back.core import security
from back.common.db import Session
from back.schemas.auth import RefreshToken

async def get_db_connection() -> Generator:
    try:
        db = Session()
        yield db
    finally:
        await db.commit()
        await db.close()


def get_user_id_by_access_token(
    credentials: HTTPAuthorizationCredentials = Security(security.bearer)
) -> int:
    try:
        token = credentials.credentials
        return security.validate_access_token(token)
    except AttributeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access токен не обнаружен"
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Данный access токен уже недействителен"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный access токен"
        )


async def get_user_id_by_refresh_token(
    token_in_form: RefreshToken, token_in_cookie: str = Cookie(None) 
) -> int:
    token = token_in_cookie if token_in_cookie else token_in_form.refresh_token
    if not token:
        # Выдаем ошибку о том что в печеньках не найдена кука
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh токен не обнаружен"
        )
    try:
        return await security.validate_refresh_token(token)
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный refresh токен"
        )


