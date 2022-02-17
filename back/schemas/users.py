from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    username: str
    avatar: str
    discriminator: str


class UserIn(BaseUser):
    discord_id: str = Field(alias="id")


class UserOutput(BaseUser):
    id: int

    class Config:
        orm_mode = True