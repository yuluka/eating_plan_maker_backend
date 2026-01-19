from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, Query

from src.db.session import get_db
from src.crud import micronutrient_group as crud
from src.schemas.micronutrient_group import MicronutrientGroupCreate, MicronutrientGroupRead, MicronutrientGroupUpdate


async def create_micronutrient_group(
    micronutrient_group: MicronutrientGroupCreate, 
    db: AsyncSession = Depends(get_db)
) -> MicronutrientGroupRead:
    """
    Create a micronutrient group into the db.
    
    :param micronutrient_group: The micronutrient group to create.
    :type micronutrient_group: MicronutrientGroupCreate
    :param db: Database session.
    :type db: AsyncSession
    :return: The created micronutrient group.
    :rtype: MicronutrientGroupRead
    """
    
    try:
        return await crud.create_micronutrient_group(micronutrient_group, db)
    
    except HTTPException as http_exc:
        raise http_exc



async def get_all_micronutrient_groups(db: AsyncSession = Depends(get_db)) -> List[MicronutrientGroupRead]:
    """
    Retrieve all micronutrient groups from the database.

    :param db: Database session.
    :type db: AsyncSession
    :return: A list with all the micronutrient groups found.
    :rtype: List[MicronutrientGroupRead]
    """
    
    try:
        return await crud.get_all_micronutrient_groups(db)
    
    except HTTPException as http_exc:
        raise http_exc



async def get_micronutrient_group_by_id(
    micronutrient_group_id: int = Query(..., description="The ID of the micronutrient group"),
    db: AsyncSession = Depends(get_db)
) -> MicronutrientGroupRead:
    """
    Retrieve a micronutrient group from the database by its id.

    :param micronutrient_group_id: The ID in the db of the micronutrient group to update.
    :type micronutrient_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    :return: The micronutrient group found.
    :rtype: MicronutrientGroupRead
    """

    try:
        return await crud.get_micronutrient_group_by_id(micronutrient_group_id, db)

    except HTTPException as http_exc:
        raise http_exc


async def update_micronutrient_group(
    micronutrient_group_update: MicronutrientGroupUpdate,
    micronutrient_group_id: int = Query(..., description="The ID of the micronutrient group"),
    db: AsyncSession = Depends(get_db)
) -> MicronutrientGroupRead:
    """
    Update a micronutrient group into the db.

    :param micronutrient_group_update: The information to update the micronutrient group.
    :type micronutrient_group_update: MicronutrientGroupUpdate
    :param micronutrient_group_id: The ID in the db of the micronutrient group to update.
    :type micronutrient_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    :return: The updated micronutrient group.
    :rtype: MicronutrientGroupRead
    :raises HTTPException: If the used name is already in use or if the micronutrient group is not found.
    """

    try:
        return await crud.update_micronutrient_group(micronutrient_group_id, micronutrient_group_update, db)
    
    except HTTPException as http_exc:
        raise http_exc



async def delete_micronutrient_group(
    micronutrient_group_id: int = Query(..., description="The ID of the micronutrient group"),
    db: AsyncSession = Depends(get_db)
) -> None:
    """
    Delete a micronutrient group from the db.

    :param micronutrient_group_id: The ID in the db of the micronutrient group to delete.
    :type micronutrient_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    """

    try:
        return await crud.delete_micronutrient_group(micronutrient_group_id, db)

    except HTTPException as http_exc:
        raise http_exc
