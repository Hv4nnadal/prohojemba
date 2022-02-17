from pydantic import BaseModel

class OAuth2Code(BaseModel):
    code: str


class TokenData(BaseModel):
    access_token: str
    token_type: str = "Bearer"