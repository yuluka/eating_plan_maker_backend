from typing import List
from src.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text


class SpecialCondition(Base):
    __tablename__ = "special_condition"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=False, unique=True)


    def to_dict(self) -> dict:
        """
        Return a dict representation of the object.
        """

        return {
            "id": self.id,
            "name": self.name,
        }
