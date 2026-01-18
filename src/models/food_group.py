from typing import List
from src.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text


class FoodGroup(Base):
    __tablename__ = "food_group"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=False, unique=True)

    # Don't exist yet
    # food_exchanges: Mapped[List["FoodExchange"]] = relationship(
    #     "FoodExchange",
    #     back_populates="food_group",
    #     cascade="all, delete-orphan",
    # )

    def to_dict(self) -> dict:
        """
        Return a dict representation of the object.
        """

        return {
            "id": self.id,
            "name": self.name,
        }
