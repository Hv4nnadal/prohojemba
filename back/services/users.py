from back.crud.users import UsersCRUD
from back.schemas.users import UserOutput
from back.services.base import BaseService

class UsersService(BaseService):
    async def get_user_by_id(self, user_id: int) -> UserOutput:
        user_data = await UsersCRUD.get(self.db_session, user_id)
        return UserOutput.from_orm(user_data)