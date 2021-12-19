"""
    Реализует работу с токенами и паролями
"""


class AuthService:
    def __init__(self):
        pass

    def generate_password_hash(self, raw_password: str) -> str:
        pass

    def compare_passwords(self, raw_password: str, password_hash: str) -> bool:
        pass

    def _generate_access_token(self, user) -> str:
        pass

    async def _generate_refresh_token(self, user) -> str:
        pass

    async def generate_tokens(self, user) -> dict:
        pass

    def validate_access_token(self, token: str) -> int:
        pass

    async def validate_refresh_token(self, token: str) -> int:
        pass
