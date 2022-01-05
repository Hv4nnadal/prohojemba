from fastapi import APIRouter

users_router = APIRouter()


@users_router.get("/@me")
async def get_current_user(

):
    pass


@users_router.get("/{user_id}")
async def get_user_by_id(
        user_id: int
):
    pass


@users_router.put("")
async def update_user(

):
    pass
