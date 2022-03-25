from back.exceptions.base import BaseServerException


class DiscordServerNotResponse(BaseServerException):
    """Сервер дискорд не доступен
    """
    pass


class DiscordGetAccessTokenException(BaseServerException):
    """Ошибка получение access токена Discord
    """
    pass


class DiscordGetUserProfileException(BaseServerException):
    """Ошибка получения профиля пользователя в Discord
    """
    pass