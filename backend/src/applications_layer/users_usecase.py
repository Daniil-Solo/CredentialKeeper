from abc import ABC, abstractmethod
from backend.src.domains_layer.users import User
from src.domains_layer.sessions import Session


class IUserService(ABC):
    @abstractmethod
    async def username_exists(self, username: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def login(self, username: str, password: str) -> Session:
        raise NotImplementedError

    @abstractmethod
    async def logout(self, session_key: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def create_new(self, username: str, password: str) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_session_key(self, session_key: str) -> User:
        raise NotImplementedError


class NoUserException(BaseException):
    pass


class UserWithSuchUsernameExistsException(BaseException):
    pass


class WrongPasswordException(BaseException):
    pass


class NoSessionWithSuchKey(BaseException):
    pass


async def login(username: str, password: str, user_service: IUserService) -> Session:
    if not await user_service.username_exists(username):
        raise NoUserException("Пользователя с данным именем не существует")
    session = await user_service.login(username, password)
    return session


async def logout(session_key: str, user_service: IUserService) -> None:
    await user_service.logout(session_key)


async def register(username: str, password: str, user_service: IUserService) -> User:
    if await user_service.username_exists(username):
        raise UserWithSuchUsernameExistsException("Пользователь с данным именем уже существует")
    user = await user_service.create_new(username, password)
    return user
