from fastapi import APIRouter, Depends, UploadFile, File, status

from back.models.titles import TitleForm
from back.crud import titles
from back.services import auth_service, image_service

titles_router = APIRouter()


@titles_router.get("")
async def get_page(
    user_id: int = Depends(auth_service.check_access_token),
    page: int = 1
):
    """Возвращает массив обьектов TitlePreview

    Args:
        page (int, optional): Номер страницы. Defaults to 1.
    """
    return await titles.all(page)


@titles_router.get("/{title_id}")
async def get_title(
    title_id: int,
    user_id: int = Depends(auth_service.check_access_token)
):
    """Возвращает полную информацию о тайтле 

    Args:
        title_id (int): [description]
    """
    return await titles.get_by_id(title_id)   


@titles_router.post("", status_code=status.HTTP_201_CREATED)
async def create_title(
    user_id: int = Depends(auth_service.check_access_token),
    title_form: TitleForm = Depends(TitleForm.as_form),
    cover: UploadFile = File(None)
): 
    if cover:
        title_form.cover = await image_service.save(cover, "covers")

    await titles.create(title_form.dict())


@titles_router.put("/{title_id}", status_code=status.HTTP_201_CREATED)
async def update_title(
    title_id: int,
    user_id: int = Depends(auth_service.check_access_token),
    title_form: TitleForm = Depends(TitleForm.as_form),
    cover: UploadFile = File(None)
):
    if cover:
        title_form.cover = await image_service.save(cover, "covers")

    await titles.update(title_id, title_form.dict())


@titles_router.delete("/{title_id}", status_code=status.HTTP_201_CREATED)
async def delete_title(
    title_id: int,
    user_id: int = Depends(auth_service.check_access_token)
):
    await titles.delete(title_id)