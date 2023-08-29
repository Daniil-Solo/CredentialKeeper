from uuid import uuid4
from dataclasses import dataclass
from datetime import timedelta
from src.domains_layer.shared import UniqueId, Date
from src.domains_layer.base import BaseDomainEntity


@dataclass
class Session(BaseDomainEntity):
    key: str
    user_id: UniqueId
    expires_at: Date


def get_expires_date(current_date: Date) -> Date:
    return current_date + timedelta(days=1)


def generate_session_key() -> str:
    return str(uuid4())


def create_session(user_id: UniqueId, key: str, expires_at: Date) -> Session:
    return Session(id=None, key=key, user_id=user_id, expires_at=expires_at)
