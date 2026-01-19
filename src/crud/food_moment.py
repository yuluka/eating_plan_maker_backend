from typing import Any, Dict, List, Optional
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.models.food_moment import FoodMoment
from src.schemas.food_moment import FoodMomentCreate, FoodMomentRead, FoodMomentUpdate


async def create_food_moment(
    food_moment: FoodMomentCreate, 
    db: AsyncSession
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

    db_food_moment = FoodMoment(
        name=food_moment.name
    )

    db.add(db_food_moment)
    
    try:
        await db.commit()
    
    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409, 
            detail="Nombre de momento alimenticio ya está en uso"
        )

    await db.refresh(db_food_moment)

    return db_food_moment


async def get_all_food_moments(
    db: AsyncSession
) -> List[FoodMomentRead]:
    """
    Retrieve all food moments from the database.

    :param db: Database session.
    :type db: AsyncSession
    :return: A list with all the food moments found.
    :rtype: List[FoodMomentRead]
    """

    result = await db.execute(
        select(FoodMoment)
    )

    db_food_moments: List[FoodMoment] = result.scalars().all()

    return db_food_moments


async def get_food_moment_by_id(
    food_moment_id: int,
    db: AsyncSession
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

    result = await db.execute(
        select(FoodMoment).where(FoodMoment.id == food_moment_id)
    )

    db_food_moment: Optional[FoodMoment] = result.scalar_one_or_none()

    if not db_food_moment:
        raise HTTPException(status_code=404, detail="Momento alimenticio no encontrado")

    return db_food_moment


async def update_food_moment(
    food_moment_id: int,
    food_moment_update: FoodMomentUpdate,
    db: AsyncSession
) -> FoodMomentRead:
    """
    Update a food moment into the db.

    :param food_moment_id: The ID in the db of the food moment to update.
    :type food_moment_id: int
    :param food_moment_update: The information to update the food moment.
    :type food_moment_update: FoodMomentUpdate
    :param db: Database session.
    :type db: AsyncSession
    :return: The updated food moment.
    :rtype: FoodMomentRead
    :raises HTTPException: If the used name is already in use or if the food moment is not found.
    """

    db_food_moment: FoodMoment = await get_food_moment_by_id(food_moment_id, db)

    resulting_food_moment: Dict[str, Any] = food_moment_update.model_dump(exclude_unset=True)
    
    for key, val in resulting_food_moment.items():
        setattr(db_food_moment, key, val)
    

    try:
        await db.commit()
    
    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409, 
            detail="Nombre de momento alimenticio ya está en uso"
        )
    

    await db.refresh(db_food_moment)
    return db_food_moment


async def delete_food_moment(
    food_moment_id: int, 
    db: AsyncSession
) -> None:
    """
    Delete a food moment from the db.

    :param food_moment_id: The ID in the db of the food moment to delete.
    :type food_moment_id: int
    :param db: Database session.
    :type db: AsyncSession
    """

    db_food_moment: FoodMoment = await get_food_moment_by_id(food_moment_id, db)

    await db.delete(db_food_moment)


    try:
        await db.commit()

    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409,
            detail="El momento alimenticio está en uso y no puede eliminarse"
        )
