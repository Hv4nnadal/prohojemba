from pydantic import BaseModel

class OAuth2Code(BaseModel):
    code: str