from sqlalchemy import Integer
import sqlalchemy.orm as so


class Base(so.DeclarativeBase):
    id: so.Mapped[int] = so.mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
