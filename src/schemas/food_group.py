from typing import Optional
from pydantic import BaseModel, Field


class FoodGroupBase(BaseModel):
    """
    Pydantic base schema for food groups to manage data validation across the application
    """

    name: str = Field(
        ...,
        description="The name of the food group (e.g. 'Frutas', 'Hortalizas')",
    )


class FoodGroupCreate(FoodGroupBase):
    """
    Pydantic schema to create the object.
    """

    pass


class FoodGroupUpdate(FoodGroupBase):
    """
    Pydantic schema to update the object.
    """

    name: Optional[str] = Field(None)


class FoodGroupRead(FoodGroupBase):
    """
    Pydantic schema to read the object.
    """

    id: int = Field(..., description="The ID of the object in the DB")

    class Config:
        from_attributes = True
