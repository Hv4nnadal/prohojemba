"""
    Реализует работу с токенами и паролями
"""
import jwt
import random
import string
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext

security = HTTPBearer(auto_error=False)


class AuthService:
    hasher = CryptContext(schemes=["bcrypt"])
    numbers = string.digits

    def __init__(self, secret_key: str):
        self.secret_key = secret_key

    def generate_password_hash(self, raw_password: str) -> str:
        return self.hasher.hash(raw_password)

    def compare_passwords(self, raw_password: str, password_hash: str) -> bool:
        return self.hasher.verify(raw_password, password_hash)

    def generate_code(self) -> str:
        """
        Генерирует вроде-как уникальный код
        :return: строка кода
        """
        return "".join(random.choice(self.numbers) for i in range(8))

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

    def _generate_refresh_token(self, user_id: int) -> str:
        payload = {
            "exp": datetime.utcnow() + timedelta(days=3),
            "scope": "refresh_token",
            "user_id": user_id
        }
        return jwt.encode(
            payload,
            self.secret_key,
            algorithm="HS256"
        )

    def generate_tokens(self, user_id: int) -> dict:
        return {
            "access_token": self._generate_access_token(user_id),
            "refresh_token": self._generate_refresh_token(user_id),
            "token_type": "Bearer"
        }

    def _parse_token(self, credentials: HTTPAuthorizationCredentials, token_type: str) -> Optional[int]:
        token = credentials.credentials
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"],)
            if payload["scope"] == token_type:
                return payload["user_id"]
            raise jwt.InvalidTokenError

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')

    def check_access_token(self, credentials: HTTPAuthorizationCredentials = Security(security)) -> Optional[int]:
        return self._parse_token(credentials, "access_token")

    def check_refresh_token(self, credentials: HTTPAuthorizationCredentials = Security(security)) -> Optional[int]:
        return self._parse_token(credentials, "refresh_token")

