from src.applications_layer.users_usecase import IUserService
from src.domains_layer.sessions import Session
from src.domains_layer.shared import UniqueId
from src.database.repositories.abstract_repository import AbstractRepository
from src.domains_layer.users import User


class IUserRepository(AbstractRepository):
    async def exists(self, username: str) -> bool:
        raise NotImplementedError

    async def get_one(self, username: str = None, password: str = None, user_id: UniqueId = None) -> User:
        raise NotImplementedError

    async def create_one(self, username: str, password: str) -> User:
        raise NotImplementedError


class ISessionRepository(AbstractRepository):
    async def create_one(self, user_id: UniqueId) -> Session:
        raise NotImplementedError

    async def remove_one(self, session_key: str) -> None:
        raise NotImplementedError

    async def get_one(self, session_key: str) -> Session:
        raise NotImplementedError


class UserService(IUserService):
    def __init__(self, user_repo: IUserRepository, session_repo: ISessionRepository):
        self.user_repo = user_repo
        self.session_repo = session_repo

    async def username_exists(self, username: str) -> bool:
        return await self.user_repo.exists(username)

    async def login(self, username: str, password: str) -> Session:
        user = await self.user_repo.get_one(username=username, password=password)
        session = await self.session_repo.create_one(user.id)
        return session

    async def logout(self, session_key: str) -> None:
        await self.session_repo.remove_one(session_key)

    async def create_new(self, username: str, password: str) -> User:
        return await self.user_repo.create_one(username, password)

    async def get_user_by_session_key(self, session_key: str) -> User:
        session = await self.session_repo.get_one(session_key)
        user = await self.user_repo.get_one(user_id=session.user_id)
        return user
