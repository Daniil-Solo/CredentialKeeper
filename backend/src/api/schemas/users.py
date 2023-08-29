from src.api.schemas.base import BaseSchema
from src.api.schemas.base_response import OkResponseSchema


class CreateUser(BaseSchema):
    username: str
    password: str


class LoginUser(BaseSchema):
    username: str
    password: str


class User(CreateUser):
    id: int


class UserResponseSchema(OkResponseSchema):
    user: User
