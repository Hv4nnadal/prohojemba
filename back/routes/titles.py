from fastapi import APIRouter

titles_router = APIRouter()


@titles_router.get("")
async def get_page(page: int = 1):
    """Возвращает массив обьектов TitlePreview

    Args:
        page (int, optional): Номер страницы. Defaults to 1.
    """
    pass


@titles_router.get("/{title_id}")
async def get_title(title_id: int):
    """Возвращает полную информацию о тайтле 

    Args:
        title_id (int): [description]
    """
    pass


@titles_router.post("")
async def create_title():
    pass


@titles_router.put("/{title_id}")
async def update_title(title_id: int):
    pass


@titles_router.delete("/{title_id}")
async def delete_title(title_id: int):
    pass