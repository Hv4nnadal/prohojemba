from pydantic import BaseModel, EmailStr


class SignInModel(BaseModel):
    username: str
    email: EmailStr
    password: str


class LogInModel(BaseModel):
    email: EmailStr
    password: str


class ChangeEmailModel(BaseModel):
    email: EmailStr
    password: str


class ChangePasswordModel(BaseModel):
    current_password: str
    new_password: str
