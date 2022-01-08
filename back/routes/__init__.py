from .auth import auth_router
from .users import users_router
from .titles import titles_router
from . import walks

routes = {
    "/auth": auth_router,
    "/users": users_router,
    "/titles": titles_router
}