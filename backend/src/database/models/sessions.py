import sqlalchemy.orm as so
from sqlalchemy import ForeignKey, Date, String
from src.database.models.base import Base
from datetime import date


class Session(Base):
    __tablename__ = "sessions"

    user_id: so.Mapped[int] = so.mapped_column(ForeignKey("users.id"), nullable=False)
    key: so.Mapped[str] = so.mapped_column(String, index=True, nullable=False)
    expires_at: so.Mapped[date] = so.mapped_column(Date, nullable=False)
