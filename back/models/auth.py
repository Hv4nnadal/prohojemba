from re import L
from typing import Optional
from pydantic import BaseModel, EmailStr, ValidationError, constr
from fastapi import Form, status
from fastapi.exceptions import HTTPException


class SignInModel(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_validated: bool = False

    @classmethod
    def as_form(cls,
                username: str = Form(None),
                email: EmailStr = Form(None),
                password: str = Form(None),
                ):
        try:
            return cls(
                username=username,
                email=email,
                password=password
            )
        except ValidationError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=e.errors()
            )


class LogInModel(BaseModel):
    email: EmailStr
    password: str
    code: Optional[constr(regex=r"\d{6}")]

    @classmethod
    def as_form(cls,
                email: EmailStr = Form(None),
                password: str = Form(None),
                code: str = Form(None)
                ):
        try:
            return cls(
                email=email,
                password=password,
                code=code
            )
        except ValidationError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=e.errors()
            )


class ChangeEmailModel(BaseModel):
    email: EmailStr
    password: str
    code: Optional[constr(regex=r"\d{6}")]

    @classmethod
    def as_form(cls,
                email: EmailStr = Form(None),
                password: str = Form(None),
                code: str = Form(None)
                ):
        try:
            return cls(
                email=email,
                password=password,
                code=code
            )
        except ValidationError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=e.errors()
            )


class ChangePasswordModel(BaseModel):
    current_password: str
    new_password: str

    @classmethod
    def as_form(cls,
                current_password: str = Form(None),
                new_password: str = Form(None),
                ):
        try:
            return cls(
                current_password=current_password,
                new_password=new_password
            )
        except ValidationError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=e.errors()
            )


class TokensResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
