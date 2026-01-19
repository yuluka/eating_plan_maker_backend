from typing import Optional
from pydantic import BaseModel, Field


class FoodMomentBase(BaseModel):
    """
    Pydantic base schema for food moments to manage data validation across the application
    """

    name: str = Field(
        ...,
        description="The name of the food moment (e.g. 'Frutas', 'Hortalizas')",
    )


class FoodMomentCreate(FoodMomentBase):
    """
    Pydantic schema to create the object.
    """

    pass


class FoodMomentUpdate(FoodMomentBase):
    """
    Pydantic schema to update the object.
    """

    name: Optional[str] = Field(None)


class FoodMomentRead(FoodMomentBase):
    """
    Pydantic schema to read the object.
    """

    id: int = Field(..., description="The ID of the object in the DB")

    class Config:
        from_attributes = True
