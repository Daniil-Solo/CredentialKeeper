from abc import ABC
from sqlalchemy.ext.asyncio import AsyncSession


class RDBRepository(ABC):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_session(self):
        return self.session
