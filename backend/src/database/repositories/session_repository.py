import datetime
from src.applications_layer.users_usecase import NoSessionWithSuchKey
from src.domains_layer.sessions import create_session, generate_session_key, get_expires_date, Session as SessionEntity
from src.database.models.sessions import Session as SessionModel
from src.domains_layer.shared import UniqueId
from src.services_layer.users_services import ISessionRepository
from src.database.repositories.rdb_repository import RDBRepository
from sqlalchemy.sql import delete, select
from src.mappers.sessions import SessionMapper


class SessionRepositoryRDB(RDBRepository, ISessionRepository):
    async def create_one(self, user_id: UniqueId) -> SessionEntity:
        expires_date = get_expires_date(datetime.datetime.today())
        session_key = generate_session_key()
        session_entity = create_session(user_id, session_key, expires_date)
        session_model = SessionMapper.from_domain_entity_to_db_model(session_entity)
        session = await self.get_session()
        session.add(session_model)
        await session.commit()
        await session.refresh(session_model)
        user_entity = SessionMapper.from_db_model_to_domain_entity(session_model)
        return user_entity

    async def remove_one(self, session_key: str) -> None:
        stmt = delete(SessionModel).where(SessionModel.key == session_key)
        session = await self.get_session()
        await session.execute(stmt)
        await session.commit()

    async def get_one(self, session_key: str) -> SessionEntity:
        query = select(SessionModel).where(SessionModel.key == session_key)
        session = await self.get_session()
        result = await session.execute(query)
        session_model = result.scalar()
        if session_model is None:
            raise NoSessionWithSuchKey("Сессии с таким ключом не существует")
        session_entity = SessionMapper.from_db_model_to_domain_entity(session_model)
        return session_entity
