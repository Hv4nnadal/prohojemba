"""
    Реализует работу с токенами и паролями
"""
import jwt
import random
import string
from aioredis import Redis
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext

from back.models.auth import TokensResponse

security = HTTPBearer(auto_error=False)


class AuthService:
    hasher = CryptContext(schemes=["bcrypt"])
    numbers = string.digits

    def __init__(self, secret_key: str, redis: Redis):
        self.redis = redis
        self.secret_key = secret_key

    def generate_password_hash(self, raw_password: str) -> str:
        return self.hasher.hash(raw_password)

    def compare_passwords(self, raw_password: str, password_hash: str) -> bool:
        return self.hasher.verify(raw_password, password_hash)

    async def generate_code(self, email: str) -> str:
        code = "".join(random.choice(string.digits) for i in range(6))
        await self.redis.set(email, code)
        return code

    async def validate_code(self, email: str, code: str) -> bool:
        saved_code = await self.redis.get(email)
        if saved_code == code.encode("utf-8"):
            print("Коды совпадают")
            await self.redis.delete(email)
            return True

        return False

    def _generate_access_token(self, user_id: int) -> str:
        payload = {
            "exp": datetime.utcnow() + timedelta(minutes=30),
            "scope": "access_token",
            "user_id": user_id
        }
        return jwt.encode(
            payload,
            self.secret_key,
            algorithm="HS256"
        )

    async def _generate_refresh_token(self, user_id: int) -> str:
        payload = {
            "exp": datetime.utcnow() + timedelta(hours=2),
            "scope": "refresh_token",
            "user_id": user_id
        }
        token = jwt.encode(
            payload,
            self.secret_key,
            algorithm="HS256"
        )
        await self.redis.set(user_id, token)
        return token

    def _parse_token(self, token: str, token_type: str) -> Optional[int]:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"],)
            if payload["scope"] == token_type:
                return payload["user_id"]
            raise jwt.InvalidTokenError

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

    async def generate_tokens(self, user_id: int) -> TokensResponse:
        access_token = self._generate_access_token(user_id)
        refresh_token = await self._generate_refresh_token(user_id)
        return TokensResponse(
            access_token=access_token,
            refresh_token=refresh_token
        )

    def check_access_token(self, credentials: HTTPAuthorizationCredentials = Security(security)) -> Optional[int]:
        try:
            token = credentials.credentials
        except AttributeError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Access token not found."
            )
        return self._parse_token(token, "access_token")

    async def check_refresh_token(self, credentials: HTTPAuthorizationCredentials = Security(security)) -> Optional[int]:
        try:
            token = credentials.credentials
        except AttributeError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token not found."
            )
        user_id = self._parse_token(token, "refresh_token")
        saved_token = await self.redis.get(user_id)

        if not saved_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is not in store.")

        if not saved_token == token.encode("utf-8"):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is not same in store.")

        return user_id



