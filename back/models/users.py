from datetime import date
from sqlalchemy import Column, BigInteger, String, Boolean, Date, DateTime

from back.common.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    username = Column("username", String(64))
    avatar = Column("avatar", String(128))
    discriminator = Column("discriminator", String(4))        


    def __init__(self, id: int, username: str, avatar: str, discriminator: str) -> None:
        super().__init__()
        self.id = id
        self.username = username
        self.avatar = f"https://cdn.discordapp.com/avatars/{id}/{avatar}.webp"
        self.discriminator = discriminator

    def update(self, id: int, username: str, avatar: str, discriminator: str):
        self.username = username
        self.avatar = f"https://cdn.discordapp.com/avatars/{id}/{avatar}.webp"
        self.discriminator = discriminator