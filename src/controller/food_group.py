from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, Query

from src.db.session import get_db
from src.crud import food_group as crud
from src.schemas.food_group import FoodGroupCreate, FoodGroupRead, FoodGroupUpdate


async def create_food_group(
    food_group: FoodGroupCreate, 
    db: AsyncSession = Depends(get_db)
) -> FoodGroupRead:
    """
    Create a food group into the db.
    
    :param food_group: The food group to create.
    :type food_group: FoodGroupCreate
    :param db: Database session.
    :type db: AsyncSession
    :return: The created food group.
    :rtype: FoodGroupRead
    """
    
    try:
        return await crud.create_food_group(food_group, db)
    
    except HTTPException as http_exc:
        raise http_exc



async def get_all_food_groups(db: AsyncSession = Depends(get_db)) -> List[FoodGroupRead]:
    """
    Retrieve all food groups from the database.

    :param db: Database session.
    :type db: AsyncSession
    :return: A list with all the food groups found.
    :rtype: List[FoodGroupRead]
    """
    
    try:
        return await crud.get_all_food_groups(db)
    
    except HTTPException as http_exc:
        raise http_exc



async def get_food_group_by_id(
    food_group_id: int = Query(..., description="The ID of the food group"),
    db: AsyncSession = Depends(get_db)
) -> FoodGroupRead:
    """
    Retrieve a food group from the database by its id.

    :param food_group_id: The ID in the db of the food group to update.
    :type food_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    :return: The food group found.
    :rtype: FoodGroupRead
    """
    try:
        return await crud.get_food_group_by_id(food_group_id, db)

    except HTTPException as http_exc:
        raise http_exc


async def update_food_group(
    food_group_update: FoodGroupUpdate,
    food_group_id: int = Query(..., description="The ID of the food group"),
    db: AsyncSession = Depends(get_db)
) -> FoodGroupRead:
    """
    Update a food group into the db.

    :param food_group_update: The information to update the food group.
    :type food_group_update: FoodGroupUpdate
    :param food_group_id: The ID in the db of the food group to update.
    :type food_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    :return: The updated food group.
    :rtype: FoodGroupRead
    :raises HTTPException: If the used name is already in use or if the food group is not found.
    """
    try:
        await crud.update_food_group(food_group_id, food_group_update, db)
    
    except HTTPException as http_exc:
        raise http_exc



async def delete_food_group(
    food_group_id: int = Query(..., description="The ID of the food group"),
    db: AsyncSession = Depends(get_db)
) -> None:
    """
    Delete a food group from the db.

    :param food_group_id: The ID in the db of the food group to delete.
    :type food_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    """

    try:
        return await crud.delete_food_group(food_group_id, db)

    except HTTPException as http_exc:
        raise http_exc
