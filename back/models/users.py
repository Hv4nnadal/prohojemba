from typing import Optional
from pydantic import BaseModel
from pydantic import ValidationError, Field
from fastapi import Form, status
from fastapi.exceptions import HTTPException

"""
    Модель пользователя для показа в собственном профиле
    Модель пользователя для показа другим пользователям
    Модель для превью
"""
class UserAuth(BaseModel):
    """
        Основная информация о пользователе
    """
    id: int
    email: str
    password: str
    is_validated: str


class ChangeUserModel(BaseModel):
    """
        Форма изменения пользовательских данных
    """
    username: str
    avatar: Optional[str]

    @classmethod
    def as_form(cls,
                username: str = Form(None)
                ):
        try:
            return cls(username=username)
        except ValidationError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=e.errors()
            )


class UserOutput(BaseModel):
    """
        Общая модель пользователя
    """
    id: int
    username: str
    email: str
    avatar: Optional[str]
    is_validated: bool


class UserPreview(BaseModel):
    """
        Краткая информация о пользователе
    """
    id: int
    username: str
    avatar: Optional[str]


class UserForWalk(UserPreview):
    id: int = Field(..., alias="user_id")