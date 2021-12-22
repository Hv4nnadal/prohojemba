from pydantic import EmailStr

from .form import FormModel

class SignInModel(FormModel):
    username: str
    email: EmailStr
    password: str


class LogInModel(FormModel):
    email: EmailStr
    password: str


class ChangeEmailModel(FormModel):
    email: EmailStr
    password: str


class ChangePasswordModel(FormModel):
    current_password: str
    new_password: str
