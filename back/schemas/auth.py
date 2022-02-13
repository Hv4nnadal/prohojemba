from pydantic import BaseModel

class OAuth2Code(BaseModel):
    code: str


class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"
    expires_at: int