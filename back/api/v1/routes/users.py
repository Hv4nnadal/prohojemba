from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from back.api import deps
from back.services.users import UsersService

router = APIRouter(prefix="/users", tags=["Профили"])


@router.get("/@me")
async def get_me(
    user_id: int = Depends(deps.get_user_id_by_access_token),
    db: AsyncSession = Depends(deps.get_db_connection)
):
    users_servcie = UsersService(db)
    return await users_servcie.get_user_by_id(user_id)


@router.get("/@me/walks")
async def get_me_walks():
    pass


@router.get("/{user_id}")
async def get_user(
    user_id: int
):
    pass


@router.get("/{user_id}/walks")
async def get_user_walks(
    user_id: int
):
    pass
