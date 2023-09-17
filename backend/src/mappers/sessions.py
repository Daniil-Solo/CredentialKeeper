from src.mappers.base import BaseMapper
from src.domains_layer.sessions import Session as SessionEntity
from src.database.models.sessions import Session as SessionModel


class SessionMapper(BaseMapper):
    @staticmethod
    def from_db_model_to_domain_entity(session: SessionModel) -> SessionEntity:
        return SessionEntity(
            id=session.id,
            key=session.key,
            user_id=session.user_id,
            expires_at=session.expires_at
        )

    @staticmethod
    def from_domain_entity_to_db_model(session: SessionEntity):
        return SessionModel(
            id=session.id,
            key=session.key,
            user_id=session.user_id,
            expires_at=session.expires_at
        )
