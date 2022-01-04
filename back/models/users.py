from typing import Optional
from pydantic import BaseModel


class ChangeUserModel(BaseModel):
    username: str
    avatar: Optional[str]


class UserOutput(BaseModel):
    id: int
    username: str
    email: str
    is_validated: bool
    password: str
