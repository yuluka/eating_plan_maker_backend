from typing import Optional
from pydantic import BaseModel, Field


class MacronutrientGroupBase(BaseModel):
    """
    Pydantic base schema for macronutrient groups to manage data validation across the application
    """

    name: str = Field(
        ...,
        description="The name of the macronutrient group (e.g. 'Carbohidrato', 'Proteína')",
    )


class MacronutrientGroupCreate(MacronutrientGroupBase):
    """
    Pydantic schema to create the object.
    """

    pass


class MacronutrientGroupUpdate(MacronutrientGroupBase):
    """
    Pydantic schema to update the object.
    """

    name: Optional[str] = Field(None)


class MacronutrientGroupRead(MacronutrientGroupBase):
    """
    Pydantic schema to read the object.
    """

    id: int = Field(..., description="The ID of the object in the DB")

    class Config:
        from_attributes = True
