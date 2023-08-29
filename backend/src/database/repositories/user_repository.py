from src.domains_layer.shared import UniqueId
from src.domains_layer.users import create_user, User as UserEntity
from src.database.models.users import User as UserModel
from src.services_layer.users_services import IUserRepository
from src.database.repositories.rdb_repository import RDBRepository
from sqlalchemy.sql import select
from sqlalchemy import and_
from src.mappers.users import UserMapper
from src.applications_layer.users_usecase import WrongPasswordException


class UserRepositoryRDB(RDBRepository, IUserRepository):
    async def exists(self, username: str) -> bool:
        query = select(UserModel).where(UserModel.username == username)
        session = await self.get_session()
        result = await session.execute(query)
        result = result.one_or_none()
        return bool(result)

    async def get_one(self, username: str = None, password: str = None, user_id: UniqueId = None) -> UserEntity:
        if user_id is not None:
            query = select(UserModel).where(UserModel.id == user_id)
        else:
            query = select(UserModel).where(and_(UserModel.username == username, UserModel.password == password))
        session = await self.get_session()
        result = await session.execute(query)
        user_model = result.scalar()
        if user_model is None and password is not None:
            raise WrongPasswordException("Неверный пароль")
        user_entity = UserMapper.from_db_model_to_domain_entity(user_model)
        return user_entity

    async def create_one(self, username: str, password: str) -> UserEntity:
        user_entity = create_user(username, password)
        user_model = UserMapper.from_domain_entity_to_db_model(user_entity)
        session = await self.get_session()
        session.add(user_model)
        await session.commit()
        await session.refresh(user_model)
        user_entity = UserMapper.from_db_model_to_domain_entity(user_model)
        return user_entity
