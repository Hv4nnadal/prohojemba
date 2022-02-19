from datetime import date
from sqlalchemy import Column, BigInteger, String, Boolean, Date, DateTime

from back.common.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    username = Column("username", String(64))
    avatar = Column("avatar", String(128))
    discriminator = Column("discriminator", String(4))        
