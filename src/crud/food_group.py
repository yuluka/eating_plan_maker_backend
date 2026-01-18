from typing import Any, Dict, List, Optional
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.models.food_group import FoodGroup
from src.schemas.food_group import FoodGroupCreate, FoodGroupRead, FoodGroupUpdate


async def create_food_group(
    food_group: FoodGroupCreate, 
    db: AsyncSession
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

    db_food_group = FoodGroup(
        name=food_group.name
    )

    db.add(db_food_group)
    
    try:
        await db.commit()
    
    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409, 
            detail="Nombre de grupo alimenticio ya está en uso"
        )

    await db.refresh(db_food_group)

    return db_food_group


async def get_all_food_groups(
    db: AsyncSession
) -> List[FoodGroupRead]:
    """
    Retrieve all food groups from the database.

    :param db: Database session.
    :type db: AsyncSession
    :return: A list with all the food groups found.
    :rtype: List[FoodGroupRead]
    """

    result = await db.execute(
        select(FoodGroup)
    )

    db_food_groups: List[FoodGroup] = result.scalars().all()

    return db_food_groups


async def get_food_group_by_id(
    food_group_id: int,
    db: AsyncSession
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

    result = await db.execute(
        select(FoodGroup).where(FoodGroup.id == food_group_id)
    )

    db_food_group: Optional[FoodGroup] = result.scalar_one_or_none()

    if not db_food_group:
        raise HTTPException(status_code=404, detail="Grupo alimenticio no encontrado")

    return db_food_group


async def update_food_group(
    food_group_id: int,
    food_group_update: FoodGroupUpdate,
    db: AsyncSession
) -> FoodGroupRead:
    """
    Update a food group into the db.

    :param food_group_id: The ID in the db of the food group to update.
    :type food_group_id: int
    :param food_group_update: The information to update the food group.
    :type food_group_update: FoodGroupUpdate
    :param db: Database session.
    :type db: AsyncSession
    :return: The updated food group.
    :rtype: FoodGroupRead
    :raises HTTPException: If the used name is already in use or if the food group is not found.
    """

    db_food_group: FoodGroup = await get_food_group_by_id(food_group_id, db)

    resulting_food_group: Dict[str, Any] = food_group_update.model_dump(exclude_unset=True)
    
    for key, val in resulting_food_group.items():
        setattr(db_food_group, key, val)
    

    try:
        await db.commit()
    
    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409, 
            detail="Nombre de grupo alimenticio ya está en uso"
        )
    

    await db.refresh(db_food_group)
    return db_food_group


async def delete_food_group(
    food_group_id: int, 
    db: AsyncSession
) -> None:
    """
    Delete a food group from the db.

    :param food_group_id: The ID in the db of the food group to delete.
    :type food_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    """

    db_food_group: FoodGroup = await get_food_group_by_id(food_group_id, db)

    await db.delete(db_food_group)


    try:
        await db.commit()

    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409,
            detail="El grupo alimenticio está en uso y no puede eliminarse"
        )
