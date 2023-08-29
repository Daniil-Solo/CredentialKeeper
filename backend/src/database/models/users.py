import sqlalchemy.orm as so
from sqlalchemy import String
from src.database.models.base import Base
from src.database.models.projects import Project


class User(Base):
    __tablename__ = "users"

    username: so.Mapped[str] = so.mapped_column(String, nullable=False, unique=True, index=True)
    password: so.Mapped[str] = so.mapped_column(String, nullable=False)
    projects: so.Mapped[list["Project"]] = so.relationship()
