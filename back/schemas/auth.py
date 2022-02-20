from pydantic import BaseModel

class OAuth2Code(BaseModel):
    code: str


class RefreshToken(BaseModel):
    refresh_token: str | None


class TokensPair(BaseModel):
    access_token: str
    expires_at: int
    token_type: str = "Bearer"
    refresh_token: str