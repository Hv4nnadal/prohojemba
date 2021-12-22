from fastapi import Request, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, ValidationError

class FormModel(BaseModel):
    @classmethod
    async def as_form(cls, request: Request):
        """
            Парсинг формы
        """
        form_data = await request.form()
        try:
            return cls(**form_data)
        except ValidationError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=e.errors()
            )