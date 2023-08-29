from dataclasses import dataclass
from src.domains_layer.base import BaseDomainEntity


@dataclass
class User(BaseDomainEntity):
    username: str
    password: str


def create_user(username: str, password: str) -> User:
    return User(id=None, username=username, password=password)
