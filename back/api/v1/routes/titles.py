from fastapi import APIRouter


router = APIRouter(prefix="/titles", tags=["Тайтлы"])


@router.get("")
async def titles_list():
    pass


@router.get("/{title_id}")
async def get_title_info(
    title_id: int
):
    pass


@router.post("")
async def create_title():
    pass


@router.put("/{title_id}")
async def update_title(
    title_id: int
):
    pass


@router.delete("/{title_id}")
async def delete_title_id(
    title_id: int
):
    pass


@router.get("/{title_id}/walks")
async def title_walks(
    title_id: int
):
    pass
