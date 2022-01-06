from fastapi import APIRouter, Depends, UploadFile, File, status
from fastapi.exceptions import HTTPException

from back.crud import users
from back.models.users import ChangeUserModel
from back.services import auth_service, image_service

users_router = APIRouter()


@users_router.get("/@me")
async def get_current_user(
        user_id: int = Depends(auth_service.check_access_token)
):
    return await users.get_by_id(user_id)


@users_router.get("/{user_id}")
async def get_user_by_id(
        user_id: int,
        current_user_id: int = Depends(auth_service.check_access_token),
):
    user = await users.get_by_id(user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found."
    )


@users_router.put("", status_code=status.HTTP_201_CREATED)
async def update_user(
    current_user_id: int = Depends(auth_service.check_access_token),
    form: ChangeUserModel = Depends(ChangeUserModel.as_form),
    avatar: UploadFile = File(None)
):
    if avatar:
        form.avatar = await image_service.save(avatar, "avatars")
    
    await users.update(current_user_id, form.dict())
