from datetime import date
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime

from back.common.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    discord_id = Column("discord_id", String(32), unique=True)
    username = Column("username", String(64))
    avatar = Column("avatar", String(128))
    discriminator = Column("discriminator", String(4))        
