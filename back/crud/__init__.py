from .users import UsersCRUD
from back.db.base import database

users = UsersCRUD(database)