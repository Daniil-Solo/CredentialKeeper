from abc import ABC
from src.database.models.base import Base
from src.domains_layer.base import BaseDomainEntity


class BaseMapper(ABC):
    @staticmethod
    def from_db_model_to_domain_entity(db_model: Base) -> BaseDomainEntity:
        pass
