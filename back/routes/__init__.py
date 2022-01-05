from .auth import auth_router
from .users import users_router

routes = {
    "/auth": auth_router,
    "/users": users_router
}