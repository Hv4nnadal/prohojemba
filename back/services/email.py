"""
    Реализует отправку email на указанную почту
"""
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig


class EmailService:
    def __init__(self, email_config: dict):
        self.conf = ConnectionConfig(**email_config)

    async def _send_email(self, email: str, email_text: str) -> None:
        """
        Внутренняя функция отправки email
        :param email:email, на который будет отправляться сообщение
        :param email_text: текст, который будет в отправленном сообщении
        :return:None
        """
        message = MessageSchema(
            subject="Prohojemba Authorization",
            recipients=[email],
            body=email_text,
            subtype="plain"
        )
        fm = FastMail(self.conf)
        await fm.send_message(message)

    async def send_activate_profile_message(self, email_to_send: str, username: str, code: str) -> None:
        await self._send_email(
            email=email_to_send,
            email_text="Код для регистрации аккаунта: {}".format(code)
        )

    async def send_update_email_message(self, email_to_send: str, username: str, code: str):
        await self._send_email(
            email=email_to_send,
            email_text="Код для обновления почты: {}".format(code)
        )
