"""
    Реализует работу с токенами и паролями
"""
import jwt
from passlib.context import CryptContext

class AuthService:
    hasher = CryptContext(schemes=["bcrypt"])

    def __init__(self, secret_key: str):
        self.secret_key = secret_key

    def generate_password_hash(self, raw_password: str) -> str:
        return self.hasher.hash(raw_password)

    def compare_passwords(self, raw_password: str, password_hash: str) -> bool:
        return True if password_hash == self.generate_password_hash(raw_password) else False

    def _generate_access_token(self, user) -> str:
        pass

    async def _generate_refresh_token(self, user) -> str:
        pass

    async def generate_tokens(self, user) -> dict:
        pass

    def validate_access_token(self, token: str) -> int:
        pass

    async def validate_refresh_token(self, token: str) -> int:
        pass
