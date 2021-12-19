from typing import Optional
from fastapi import APIRouter, Form, Depends, File, UploadFile ,status
from fastapi.exceptions import HTTPException
from pydantic import ValidationError

from back.models.auth import SignInModel, LogInModel

auth_router = APIRouter()


async def _parse_register_form(
    username: str = Form(None),
    email: str = Form(None),
    password: str = Form(None)
) -> SignInModel:
    try:
        return SignInModel(
            username=username,
            email=email,
            password=password
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.errors()
        )


async def _parse_login_form(
        email: str = Form(None),
        password: str = Form(None)
) -> LogInModel:
    try:
        return LogInModel(
            email=email,
            password=password
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.errors()
        )


# Регистрация нового пользователя
@auth_router.post("/sign-in")
async def sign_in(
        auth_form: SignInModel = Depends(_parse_register_form),
):
    pass


# Получение токенов пользователю по логину и паролю или по refresh_token
@auth_router.post("/token")
async def get_auth_tokens(auth_form: LogInModel = Depends(_parse_login_form)):
    print(auth_form.email)
    return {"status": True}


# Активация пользователя по коду, отправленному по почте
@auth_router.get("/activate")
async def activate_new_user():
    pass


# Изманение пароля пользователя
@auth_router.put("/change-password")
async def change_password():
    pass


# Измененение email пользователя
@auth_router.put("/change-email")
async def change_email():
    pass
