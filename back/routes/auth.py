from typing import Optional
from fastapi import APIRouter, Depends, BackgroundTasks, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from back.models.auth import SignInModel, LogInModel, ChangeEmailModel, ChangePasswordModel
from back.crud import users
from back.services import auth_service, email_service

auth_router = APIRouter(tags=["Авторизация и аутентификация"])


@auth_router.post("/signin", status_code=status.HTTP_201_CREATED)
async def sign_in(
        auth_form: SignInModel = Depends(SignInModel.as_form)
):
    """
    Обработчик запроса на создание нового профиля
    """
    auth_form.password = auth_service.generate_password_hash(auth_form.password)
    data = auth_form.dict()
    await users.create(data)


# Получение токенов с email и паролем
@auth_router.post("/login")
async def login(
        background_tasks: BackgroundTasks,
        auth_form: Optional[LogInModel] = Depends(LogInModel.as_form)):
    """
    Выполнение входа при помощи почты и пароля
    с возможной активацией профиля
    """
    # Поиск пользователя в базе данных и сравнение паролей
    user = await users.get_by_email(auth_form.email)
    if user and auth_service.compare_passwords(auth_form.password, user.password):
        # Проверка на то что профиль активен
        if user.is_validated:
            return await auth_service.generate_tokens(user.id)

        # Активация профиля по коду, отправленному на почту
        if auth_form.code:
            if await auth_service.validate_code(auth_form.email, auth_form.code):
                await users.update(user.id, {"is_validated": True})
                return await auth_service.generate_tokens(user.id)

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный код активации."
            )

        # Генерация кода активации и отправка в сообщении на email
        activation_code = await auth_service.generate_code(auth_form.email)
        background_tasks.add_task(
            email_service.send_activate_profile_message,
            email_to_send=user.email, username=user.username, code=activation_code
        )

        # ! Ошибку не кидать, фоновая задача закрывается до завершения
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "Требуется активировать профиль. Код отправлен на почту."}
        )

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Email или пароль неверны."
    )


# Обновление токенов при помощи refresh токена
@auth_router.post("/token")
async def get_auth_tokens(
        user_id: Optional[int] = Depends(auth_service.check_refresh_token),

):
    return await auth_service.generate_tokens(user_id)


# Изманение пароля пользователя
@auth_router.put("/change-password", status_code=status.HTTP_201_CREATED)
async def change_password(
        user_id: Optional[int] = Depends(auth_service.check_access_token),
        password_form: ChangePasswordModel = Depends(ChangePasswordModel.as_form)
):
    user = await users.get_by_id(user_id)
    if user and auth_service.compare_passwords(password_form.current_password, user.password):
        await users.update(user_id, {
            "password": auth_service.generate_password_hash(password_form.new_password)
        })
        return

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверный текущий пароль."
    )


# Измененение email пользователя
@auth_router.put("/change-email", status_code=status.HTTP_201_CREATED)
async def change_email(
        background_tasks: BackgroundTasks,
        user_id: Optional[int] = Depends(auth_service.check_access_token),
        email_form: ChangeEmailModel = Depends(ChangeEmailModel.as_form)
):
    user = await users.get_by_id(user_id)
    if user and auth_service.compare_passwords(email_form.password, user.password):
        if email_form.code:
            if await auth_service.validate_code(user.email, email_form.code):
                await users.update(user.id, {"is_validated": True})
                return

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный код активации."
            )

        await users.update(user_id, {
            "email": email_form.email,
            "is_validated": False
        })

        activation_code = await auth_service.generate_code(email_form.email)
        background_tasks.add_task(
            email_service.send_update_email_message,
            email_to_send=email_form.email, username=user.username, code=activation_code
        )
        # ! Ошибку не кидать, фоновая задача закрывается до завершения
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "Требуется активировать профиль. Код отправлен на почту."}
        )

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверный текущий пароль."
    )
