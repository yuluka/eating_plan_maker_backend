from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, Query

from src.db.session import get_db
from src.crud import food_moment as crud
from src.schemas.food_moment import FoodMomentCreate, FoodMomentRead, FoodMomentUpdate


async def create_food_moment(
    food_moment: FoodMomentCreate, 
    db: AsyncSession = Depends(get_db)
) -> FoodMomentRead:
    """
    Create a food moment into the db.
    
    :param food_moment: The food moment to create.
    :type food_moment: FoodMomentCreate
    :param db: Database session.
    :type db: AsyncSession
    :return: The created food moment.
    :rtype: FoodMomentRead
    """
    
    try:
        return await crud.create_food_moment(food_moment, db)
    
    except HTTPException as http_exc:
        raise http_exc



async def get_all_food_moments(db: AsyncSession = Depends(get_db)) -> List[FoodMomentRead]:
    """
    Retrieve all food moments from the database.

    :param db: Database session.
    :type db: AsyncSession
    :return: A list with all the food moments found.
    :rtype: List[FoodMomentRead]
    """
    
    try:
        return await crud.get_all_food_moments(db)
    
    except HTTPException as http_exc:
        raise http_exc



async def get_food_moment_by_id(
    food_moment_id: int = Query(..., description="The ID of the food moment"),
    db: AsyncSession = Depends(get_db)
) -> FoodMomentRead:
    """
    Retrieve a food moment from the database by its id.

    :param food_moment_id: The ID in the db of the food moment to update.
    :type food_moment_id: int
    :param db: Database session.
    :type db: AsyncSession
    :return: The food moment found.
    :rtype: FoodMomentRead
    """
    try:
        return await crud.get_food_moment_by_id(food_moment_id, db)

    except HTTPException as http_exc:
        raise http_exc


async def update_food_moment(
    food_moment_update: FoodMomentUpdate,
    food_moment_id: int = Query(..., description="The ID of the food moment"),
    db: AsyncSession = Depends(get_db)
) -> FoodMomentRead:
    """
    Update a food moment into the db.

    :param food_moment_update: The information to update the food moment.
    :type food_moment_update: FoodMomentUpdate
    :param food_moment_id: The ID in the db of the food moment to update.
    :type food_moment_id: int
    :param db: Database session.
    :type db: AsyncSession
    :return: The updated food moment.
    :rtype: FoodMomentRead
    :raises HTTPException: If the used name is already in use or if the food moment is not found.
    """
    try:
        return await crud.update_food_moment(food_moment_id, food_moment_update, db)
    
    except HTTPException as http_exc:
        raise http_exc



async def delete_food_moment(
    food_moment_id: int = Query(..., description="The ID of the food moment"),
    db: AsyncSession = Depends(get_db)
) -> None:
    """
    Delete a food moment from the db.

    :param food_moment_id: The ID in the db of the food moment to delete.
    :type food_moment_id: int
    :param db: Database session.
    :type db: AsyncSession
    """

    try:
        return await crud.delete_food_moment(food_moment_id, db)

    except HTTPException as http_exc:
        raise http_exc
