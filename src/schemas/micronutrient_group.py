from typing import Optional
from pydantic import BaseModel, Field


class MicronutrientGroupBase(BaseModel):
    """
    Pydantic base schema for micronutrient groups to manage data validation across the application
    """

    name: str = Field(
        ...,
        description="The name of the micronutrient group (e.g. 'Vitamina A', 'Vitamina C')",
    )


class MicronutrientGroupCreate(MicronutrientGroupBase):
    """
    Pydantic schema to create the object.
    """

    pass


class MicronutrientGroupUpdate(MicronutrientGroupBase):
    """
    Pydantic schema to update the object.
    """

    name: Optional[str] = Field(None)


class MicronutrientGroupRead(MicronutrientGroupBase):
    """
    Pydantic schema to read the object.
    """

    id: int = Field(..., description="The ID of the object in the DB")

    class Config:
        from_attributes = True
