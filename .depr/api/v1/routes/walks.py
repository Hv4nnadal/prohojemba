from fastapi import APIRouter


router = APIRouter(prefix="/walks", tags=["Прохождения"])


@router.post("")
async def create_walk():
    pass


@router.put("/{walk_id}")
async def update_walk():
    pass


@router.delete("/{walk_id}")
async def delete_walk():
    pass