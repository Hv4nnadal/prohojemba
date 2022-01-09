from typing import Optional
from pydantic import BaseModel
from pydantic import ValidationError, Field
from fastapi import Form, status
from fastapi.exceptions import HTTPException


class ChangeUserModel(BaseModel):
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
    id: int
    username: str
    email: str
    avatar: Optional[str]
    is_validated: bool
    password: str


class UserPreview(BaseModel):
    id: int
    username: str
    avatar: Optional[str]


class UserForWalk(UserPreview):
    id: int = Field(..., alias="user_id")