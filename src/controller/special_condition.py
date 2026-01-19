from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, Query

from src.db.session import get_db
from src.crud import special_condition as crud
from src.schemas.special_condition import SpecialConditionCreate, SpecialConditionRead, SpecialConditionUpdate


async def create_special_condition(
    special_condition: SpecialConditionCreate, 
    db: AsyncSession = Depends(get_db)
) -> SpecialConditionRead:
    """
    Create a micronutrient group into the db.
    
    :param special_condition: The micronutrient group to create.
    :type special_condition: SpecialConditionCreate
    :param db: Database session.
    :type db: AsyncSession
    :return: The created micronutrient group.
    :rtype: SpecialConditionRead
    """
    
    try:
        return await crud.create_special_condition(special_condition, db)
    
    except HTTPException as http_exc:
        raise http_exc



async def get_all_special_conditions(db: AsyncSession = Depends(get_db)) -> List[SpecialConditionRead]:
    """
    Retrieve all micronutrient groups from the database.

    :param db: Database session.
    :type db: AsyncSession
    :return: A list with all the micronutrient groups found.
    :rtype: List[SpecialConditionRead]
    """
    
    try:
        return await crud.get_all_special_conditions(db)
    
    except HTTPException as http_exc:
        raise http_exc



async def get_special_condition_by_id(
    special_condition_id: int = Query(..., description="The ID of the micronutrient group"),
    db: AsyncSession = Depends(get_db)
) -> SpecialConditionRead:
    """
    Retrieve a micronutrient group from the database by its id.

    :param special_condition_id: The ID in the db of the micronutrient group to update.
    :type special_condition_id: int
    :param db: Database session.
    :type db: AsyncSession
    :return: The micronutrient group found.
    :rtype: SpecialConditionRead
    """

    try:
        return await crud.get_special_condition_by_id(special_condition_id, db)

    except HTTPException as http_exc:
        raise http_exc


async def update_special_condition(
    special_condition_update: SpecialConditionUpdate,
    special_condition_id: int = Query(..., description="The ID of the micronutrient group"),
    db: AsyncSession = Depends(get_db)
) -> SpecialConditionRead:
    """
    Update a micronutrient group into the db.

    :param special_condition_update: The information to update the micronutrient group.
    :type special_condition_update: SpecialConditionUpdate
    :param special_condition_id: The ID in the db of the micronutrient group to update.
    :type special_condition_id: int
    :param db: Database session.
    :type db: AsyncSession
    :return: The updated micronutrient group.
    :rtype: SpecialConditionRead
    :raises HTTPException: If the used name is already in use or if the micronutrient group is not found.
    """

    try:
        return await crud.update_special_condition(special_condition_id, special_condition_update, db)
    
    except HTTPException as http_exc:
        raise http_exc



async def delete_special_condition(
    special_condition_id: int = Query(..., description="The ID of the micronutrient group"),
    db: AsyncSession = Depends(get_db)
) -> None:
    """
    Delete a micronutrient group from the db.

    :param special_condition_id: The ID in the db of the micronutrient group to delete.
    :type special_condition_id: int
    :param db: Database session.
    :type db: AsyncSession
    """

    try:
        return await crud.delete_special_condition(special_condition_id, db)

    except HTTPException as http_exc:
        raise http_exc
