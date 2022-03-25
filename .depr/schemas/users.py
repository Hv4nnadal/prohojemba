from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    id: int
    username: str
    avatar: str
    discriminator: str


class UserIn(BaseUser):
    pass


class UserOutput(BaseUser):
    class Config:
        orm_mode = True