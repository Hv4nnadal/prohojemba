from pydantic import BaseModel, EmailStr, constr


class UserCreate(BaseModel):
    """JSON схема для создания нового пользователя
    """
    username: constr(min_length=4, max_length=64)
    email: EmailStr
    password: constr(min_length=8)
