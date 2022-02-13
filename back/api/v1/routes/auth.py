from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from back.api import deps
from back.schemas.auth import OAuth2Code

router = APIRouter(prefix="/auth", tags=["Авторизация"])


@router.post("/discord")
async def auth_from_discord(
    oauth_form: OAuth2Code,
    db: AsyncSession = Depends(deps.get_db_connection)
):
    pass


@router.post("/token")
async def update_token():
    pass