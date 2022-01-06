from fastapi import UploadFile

from .base import ImageBase


class LocalImage(ImageBase):
    """Сохраняет изображения локально на сервере
    """
    def __init__(self, path: str) -> None:
        self.path = path

    async def save(self, file: UploadFile, subdir: str) -> str:
        with open(f"{self.path}/{subdir}/{file.filename}", "wb") as f:
            f.write(file.file.read())

        return f"/{subdir}/{file.filename}"