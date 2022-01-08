from typing import List
from datetime import date
from fastapi import Depends, status
from fastapi.exceptions import HTTPException

from .users import users_router
from .titles import titles_router
from back.crud import walks
from back.models.walks import WalkWithTitleInfo, WalkWithUserInfo, WalkForm
from back.services import auth_service


@users_router.get("/@me/walks", response_class=List[WalkWithTitleInfo])
async def get_current_user_walks(
        user_id: int = Depends(auth_service.check_access_token)
):
    return await walks.get_by_user_id(user_id)


@users_router.get("/{user_id}/walks", response_class=List[WalkWithTitleInfo])
async def get_user_walks(
        user_id: int,
        current_user_id: int = Depends(auth_service.check_access_token)
):
    return await walks.get_by_user_id(user_id)


@users_router.put("/@me/walks/{walk_id}", status_code=status.HTTP_201_CREATED)
async def update_current_user_walk(
        walk_id: int,
        user_id: int = Depends(auth_service.check_access_token),
        walk_form: WalkForm = Depends(WalkForm.as_form)
):
    await walks.update(walk_id, walk_form.dict())


@users_router.delete("/@me/walks/{walk_id}", status_code=status.HTTP_201_CREATED)
async def delete_current_user_walk(
        walk_id: int,
        user_id: int = Depends(auth_service.check_access_token)
):
    await walks.delete(walk_id)


@titles_router.get("/{title_id}/walks", response_class=List[WalkWithUserInfo])
async def get_title_walks(
        title_id: int,
        user_id: int = Depends(auth_service.check_access_token)
):
    return await walks.get_by_title_id(title_id)


@titles_router.post("/{title_id}/walks", status_code=status.HTTP_201_CREATED)
async def create_title_walk(
        title_id: int,
        user_id: int = Depends(auth_service.check_access_token),
        walk_form: WalkForm = Depends(WalkForm.as_form)
):
    walk_data = walk_form.dict()
    walk_data["title_id"] = title_id
    walk_data["user_id"] = user_id
    walk_data["created_at"] = date.today()
    await walks.create(walk_data)
