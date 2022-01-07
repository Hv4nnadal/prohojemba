from .users import UsersCRUD
from .titles import TitlesCRUD
from back.db.base import database

users = UsersCRUD(database)
titles = TitlesCRUD(database)