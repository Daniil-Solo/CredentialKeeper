from typing import Annotated
from fastapi import Depends, Cookie, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.applications_layer.users_usecase import IUserService, NoSessionWithSuchKey
from src.database.db import get_db_session
from src.database.repositories.user_repository import UserRepositoryRDB
from src.database.repositories.session_repository import SessionRepositoryRDB
from src.services_layer.users_services import UserService
from src.domains_layer.users import User as UserEntity


def get_user_service(session: Annotated[AsyncSession, Depends(get_db_session)]) -> IUserService:
    user_repo = UserRepositoryRDB(session)
    session_repo = SessionRepositoryRDB(session)
    user_service = UserService(user_repo, session_repo)
    return user_service


async def get_user(session_key: str = Cookie(default=''), user_service=Depends(get_user_service)) -> UserEntity:
    try:
        user = await user_service.get_user_by_session_key(session_key)
        return user
    except NoSessionWithSuchKey:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Требуется выполнить вход")
