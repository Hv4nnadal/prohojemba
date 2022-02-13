from fastapi import APIRouter

from back.api.v1.routes import auth, users, titles


v1_router = APIRouter()
v1_router.include_router(auth.router)
v1_router.include_router(users.router)
v1_router.include_router(titles.router)