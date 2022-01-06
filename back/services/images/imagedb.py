from fastapi import UploadFile

from .base import ImageBase


class ImageBB(ImageBase):
    def __init__(self, token: str) -> None:
        self.token = token

    async def save(file: UploadFile) -> str:
        pass