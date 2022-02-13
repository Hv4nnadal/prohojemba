from datetime import date
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime

from back.common.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    username = Column("username", String(64), unique=True)
    email = Column("email", String(64), unique=True, index=True)
    avatar = Column("avatar", String(128), nullable=True)
    password = Column("password", String(128))

    is_validated = Column("is_validated", Boolean, default=False)
    is_banned = Column("is_banned", Boolean, default=True)
    created_at = Column("created_at", Date, default=date.today())
    last_login = Column("last_login", DateTime)
