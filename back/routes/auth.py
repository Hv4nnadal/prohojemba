from typing import Optional
from fastapi import APIRouter, Depends, Query, status
from fastapi.exceptions import HTTPException
from pydantic import ValidationError

from back.models.auth import SignInModel, LogInModel, TokensResponse
from back.crud import users
from back.services import auth_service

auth_router = APIRouter()


# Регистрация нового пользователя
@auth_router.post("/signin")
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


# Получение токенов с email и паролем
@auth_router.post("/login", response_model=TokensResponse)
async def login(auth_form: Optional[LogInModel] = Depends(LogInModel.as_form)):
    user = await users.get_by_email(auth_form.email)
    if user and auth_service.compare_passwords(auth_form.password, user.password):
        return auth_service.generate_tokens(user.id)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User email or password incorrect"
    )


# Обновление токенов при помощи refresh токена
@auth_router.post("/token")
async def get_auth_tokens(
            user_id: Optional[int] = Depends(auth_service.check_refresh_token)
        ):
    return auth_service.generate_tokens(user_id)


# Активация пользователя по коду, отправленному по почте
@auth_router.post("/activate")
async def activate_new_user(code: int):
    # TODO получить id пользователя по коду активации в redis или словаре
    pass


# Изманение пароля пользователя
@auth_router.put("/change-password")
async def change_password():
    pass


# Измененение email пользователя
@auth_router.put("/change-email")
async def change_email():
    pass
