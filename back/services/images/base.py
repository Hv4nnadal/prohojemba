from fastapi import UploadFile

class ImageBase:
    def _verify() -> bool:
        return True

    async def save(file: UploadFile) -> str:
        """Сохраняет файл и возвращает ссылку на файл

        Returns:
            str: Ссылка на файл для доступа извне
        """
        pass
