from typing import Optional, Literal
from pydantic import BaseModel, ValidationError

from back import settings

class TitleForm(BaseModel):
    name: str
    cover: Optional[str]
    description: Optional[str]
    type: settings.TITLE_TYPES
    release_year: int


class TitlePreview(BaseModel):
    id: int
    name: str
    cover: Optional[str]
    type: str
    release_year: int
    positive_rates_count: int
    negative_rates_count: int

class TitleInfo(BaseModel):
    id: int
    name: str
    cover: Optional[str]
    description: Optional[str]
    type: str
    release_year: int
    positive_rates_count: int
    negative_rates_count: int
    