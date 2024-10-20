from datetime import datetime

from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base, CommonMixin


class Cadastre(CommonMixin, Base):
    cadastre_number: Mapped[str] = mapped_column(String)
    latitude: Mapped[str] = mapped_column(String)
    longitude: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    answer: Mapped[bool] = mapped_column(Boolean)

    def __repr__(self):
        return (
            f'Создано {self.created_at}.'
        )
