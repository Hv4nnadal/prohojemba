from .users import users_router
from .titles import titles_router


@users_router.get("/@me/walks")
async def get_current_user_walks(

):
    return {"status": True}


@users_router.get("/{user_id}/walks")
async def get_user_walks():
    return {"status": True}


@users_router.put("/@me/walks/{walk_id}")
async def update_current_user_walk(

):
    pass


@users_router.delete("/@me/walks/{walk_id}")
async def delete_current_user_walk(

):
    pass


@titles_router.get("/{title_id}/walks")
async def get_title_walks(

):
    pass


@titles_router.post("/{title_id}/walks")
async def create_title_walk():
    pass
