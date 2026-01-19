from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, Query

from src.db.session import get_db
from src.crud import macronutrient_group as crud
from src.schemas.macronutrient_group import MacronutrientGroupCreate, MacronutrientGroupRead, MacronutrientGroupUpdate


async def create_macronutrient_group(
    macronutrient_group: MacronutrientGroupCreate, 
    db: AsyncSession = Depends(get_db)
) -> MacronutrientGroupRead:
    """
    Create a macronutrient group into the db.
    
    :param macronutrient_group: The macronutrient group to create.
    :type macronutrient_group: MacronutrientGroupCreate
    :param db: Database session.
    :type db: AsyncSession
    :return: The created macronutrient group.
    :rtype: MacronutrientGroupRead
    """
    
    try:
        return await crud.create_macronutrient_group(macronutrient_group, db)
    
    except HTTPException as http_exc:
        raise http_exc



async def get_all_macronutrient_groups(db: AsyncSession = Depends(get_db)) -> List[MacronutrientGroupRead]:
    """
    Retrieve all macronutrient groups from the database.

    :param db: Database session.
    :type db: AsyncSession
    :return: A list with all the macronutrient groups found.
    :rtype: List[MacronutrientGroupRead]
    """
    
    try:
        return await crud.get_all_macronutrient_groups(db)
    
    except HTTPException as http_exc:
        raise http_exc



async def get_macronutrient_group_by_id(
    macronutrient_group_id: int = Query(..., description="The ID of the macronutrient group"),
    db: AsyncSession = Depends(get_db)
) -> MacronutrientGroupRead:
    """
    Retrieve a macronutrient group from the database by its id.

    :param macronutrient_group_id: The ID in the db of the macronutrient group to update.
    :type macronutrient_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    :return: The macronutrient group found.
    :rtype: MacronutrientGroupRead
    """

    try:
        return await crud.get_macronutrient_group_by_id(macronutrient_group_id, db)

    except HTTPException as http_exc:
        raise http_exc


async def update_macronutrient_group(
    macronutrient_group_update: MacronutrientGroupUpdate,
    macronutrient_group_id: int = Query(..., description="The ID of the macronutrient group"),
    db: AsyncSession = Depends(get_db)
) -> MacronutrientGroupRead:
    """
    Update a macronutrient group into the db.

    :param macronutrient_group_update: The information to update the macronutrient group.
    :type macronutrient_group_update: MacronutrientGroupUpdate
    :param macronutrient_group_id: The ID in the db of the macronutrient group to update.
    :type macronutrient_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    :return: The updated macronutrient group.
    :rtype: MacronutrientGroupRead
    :raises HTTPException: If the used name is already in use or if the macronutrient group is not found.
    """

    try:
        return await crud.update_macronutrient_group(macronutrient_group_id, macronutrient_group_update, db)
    
    except HTTPException as http_exc:
        raise http_exc



async def delete_macronutrient_group(
    macronutrient_group_id: int = Query(..., description="The ID of the macronutrient group"),
    db: AsyncSession = Depends(get_db)
) -> None:
    """
    Delete a macronutrient group from the db.

    :param macronutrient_group_id: The ID in the db of the macronutrient group to delete.
    :type macronutrient_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    """

    try:
        return await crud.delete_macronutrient_group(macronutrient_group_id, db)

    except HTTPException as http_exc:
        raise http_exc
