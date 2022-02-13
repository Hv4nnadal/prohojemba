import jwt
from fastapi.security import HTTPBearer
from passlib.context import CryptContext

from back.core import config


hasher = CryptContext(schemes=["bcrypt"])
bearer = HTTPBearer(auto_error=False)


def generate_access_token(user_id: int) -> str:
    """Генерация access токена, содаржащего id пользователя, дату истечения и тип токена

    Args:
        user_id (int): ID пользователя в базе данных

    Returns:
        str: Строка, содержащая токен
    """
    pass


def validate_access_token(token: str) -> int:
    """Расшифровка access токена, его валидация и получение id пользователя
    """
    payload = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
    if user_id := payload.get("user_Id"):
        return user_id
    raise jwt.InvalidTokenError


async def generate_refresh_token(user_id: int) -> str:
    pass


async def validate_refresh_token(token: str) -> int:
    pass