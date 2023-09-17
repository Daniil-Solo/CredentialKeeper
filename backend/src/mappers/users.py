from src.mappers.base import BaseMapper
from src.domains_layer.users import User as UserEntity
from src.database.models.users import User as UserModel
from src.api.schemas.users import User as UserSchema


class UserMapper(BaseMapper):
    @staticmethod
    def from_db_model_to_domain_entity(user: UserModel) -> UserEntity:
        return UserEntity(
            id=user.id,
            username=user.username,
            password=user.password
        )

    @staticmethod
    def from_domain_entity_to_db_model(user: UserEntity):
        return UserModel(
            id=user.id,
            username=user.username,
            password=user.password
        )

    @staticmethod
    def from_domain_entity_to_schema(user: UserEntity):
        return UserSchema(
            id=user.id,
            username=user.username,
            password=user.password
        )
