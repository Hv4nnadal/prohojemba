from typing import Optional
from fastapi import APIRouter, Form, Depends, status
from fastapi.exceptions import HTTPException
from pydantic import ValidationError

from back.models.auth import SignInModel, LogInModel
from back.crud import users
from back.services import auth_service

auth_router = APIRouter()


# Регистрация нового пользователя
@auth_router.post("/sign-in")
async def sign_in(
        auth_form: SignInModel = Depends(SignInModel.as_form),
        ):
    # todo Добавить генерацию кода, созданию соотношения code -> user в Redis, отправку email для активации профиля пользователя
    # Изменение поля пароля в модели пользователя на хэш текущего значения
    auth_form.password = auth_service.generate_password_hash(auth_form.password)
    # Сохранение модели пользователя
    data = auth_form.dict()

    await users.create(data)

    return auth_form


@auth_router.post("login")
async def login(auth_form: Optional[LogInModel] = Depends(LogInModel.as_form)):
    pass


# Получение токенов пользователю по логину и паролю или по refresh_token
@auth_router.post("/token")
async def get_auth_tokens(
            auth_form: Optional[LogInModel] = Depends(LogInModel.as_form),
            user_id: Optional[int] = Depends(auth_service.check_refresh_token)
        ):
    user_id = user_id if user_id else await users.get_by_email()

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


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
