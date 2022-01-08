from typing import Optional
from fastapi import Form, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, ValidationError


class TitleForm(BaseModel):
    name: str
    cover: Optional[str]
    description: Optional[str]
    type: str
    release_year: int

    @classmethod
    def as_form(cls,
                name: str = Form(None),
                description: str = Form(None),
                type: str = Form(None),
                release_year: int = Form(None)
                ):
        try:
            return cls(
                name=name,
                description=description,
                type=type,
                release_year=release_year
            )
        except ValidationError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=e.errors()
            )


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
