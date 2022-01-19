from typing import List, Optional, Sequence
from datetime import date
from pydantic import BaseModel, ValidationError
from fastapi import Form
from fastapi import status as http_status
from fastapi.exceptions import HTTPException

from .users import UserForWalk
from .titles import TitleForWalk


class WalkForm(BaseModel):
    """
        Форма добавления или редактирования информации о проходжембе
    """
    status: str
    comment: str
    rate: Optional[bool]

    @classmethod
    def as_form(cls,
                status: str = Form(None),
                comment: str = Form(None),
                rate: bool = Form(None)
                ):
        try:
            return cls(
                status=status,
                comment=comment,
                rate=rate
            )
        except ValidationError as e:
            raise HTTPException(
                status_code=http_status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=e.errors()
            )


class WalkWithUserInfo(BaseModel):
    """
        Запись о прохождении с информацией о тайтле
    """
    id: int
    user: Optional[UserForWalk]
    status: str
    comment: str
    rate: Optional[bool]
    created_at: date


class WalkWithTitleInfo(BaseModel):
    """
        Запись о прохождении с информацией о тайтле
    """
    id: int
    title: Optional[TitleForWalk]
    status: str
    comment: str
    rate: Optional[bool]
    created_at: date


class WalksList(BaseModel):
    """
        Список проходжемб
    """
    items: List[Sequence[WalkWithTitleInfo, WalkWithUserInfo]]
