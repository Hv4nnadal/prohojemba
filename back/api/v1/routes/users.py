from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["Профили"])


@router.get("/@me")
async def get_me():
    pass


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
