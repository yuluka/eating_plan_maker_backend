from typing import Optional
from pydantic import BaseModel, Field


class SpecialConditionBase(BaseModel):
    """
    Pydantic base schema for special conditions to manage data validation across the application
    """

    name: str = Field(
        ...,
        description="The name of the special condition (e.g. 'Enfermedad Real', 'Diabetes')",
    )


class SpecialConditionCreate(SpecialConditionBase):
    """
    Pydantic schema to create the object.
    """

    pass


class SpecialConditionUpdate(SpecialConditionBase):
    """
    Pydantic schema to update the object.
    """

    name: Optional[str] = Field(None)


class SpecialConditionRead(SpecialConditionBase):
    """
    Pydantic schema to read the object.
    """

    id: int = Field(..., description="The ID of the object in the DB")

    class Config:
        from_attributes = True
