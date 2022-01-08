from .users import UsersCRUD
from .titles import TitlesCRUD
from .walks import WalksCRUD
from back.db.base import database

users = UsersCRUD(database)
titles = TitlesCRUD(database)
walks = WalksCRUD(database)