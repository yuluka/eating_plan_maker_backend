from typing import Any, Dict, List, Optional
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.models.special_condition import SpecialCondition
from src.schemas.special_condition import SpecialConditionCreate, SpecialConditionRead, SpecialConditionUpdate


async def create_special_condition(
    special_condition: SpecialConditionCreate, 
    db: AsyncSession
) -> SpecialConditionRead:
    """
    Create a special condition into the db.

    :param special_condition: The special condition to create.
    :type special_condition: SpecialConditionCreate
    :param db: Database session.
    :type db: AsyncSession
    :return: The created special condition.
    :rtype: SpecialConditionRead
    """

    db_special_condition = SpecialCondition(
        name=special_condition.name
    )

    db.add(db_special_condition)
    
    try:
        await db.commit()
    
    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409, 
            detail="Nombre de condición especial ya está en uso"
        )

    await db.refresh(db_special_condition)

    return db_special_condition


async def get_all_special_conditions(
    db: AsyncSession
) -> List[SpecialConditionRead]:
    """
    Retrieve all special conditions from the database.

    :param db: Database session.
    :type db: AsyncSession
    :return: A list with all the special conditions found.
    :rtype: List[SpecialConditionRead]
    """

    result = await db.execute(
        select(SpecialCondition)
    )

    db_special_conditions: List[SpecialCondition] = result.scalars().all()

    return db_special_conditions


async def get_special_condition_by_id(
    special_condition_id: int,
    db: AsyncSession
) -> SpecialConditionRead:
    """
    Retrieve a special condition from the database by its id.

    :param special_condition_id: The ID in the db of the special condition to update.
    :type special_condition_id: int
    :param db: Database session.
    :type db: AsyncSession
    :return: The special condition found.
    :rtype: SpecialConditionRead
    """

    result = await db.execute(
        select(SpecialCondition).where(SpecialCondition.id == special_condition_id)
    )

    db_special_condition: Optional[SpecialCondition] = result.scalar_one_or_none()

    if not db_special_condition:
        raise HTTPException(status_code=404, detail="Condición especial no encontrada")

    return db_special_condition


async def update_special_condition(
    special_condition_id: int,
    special_condition_update: SpecialConditionUpdate,
    db: AsyncSession
) -> SpecialConditionRead:
    """
    Update a special condition into the db.

    :param special_condition_id: The ID in the db of the special condition to update.
    :type special_condition_id: int
    :param special_condition_update: The information to update the special condition.
    :type special_condition_update: SpecialConditionUpdate
    :param db: Database session.
    :type db: AsyncSession
    :return: The updated special condition.
    :rtype: SpecialConditionRead
    :raises HTTPException: If the used name is already in use or if the special condition is not found.
    """

    db_special_condition: SpecialCondition = await get_special_condition_by_id(special_condition_id, db)

    resulting_special_condition: Dict[str, Any] = special_condition_update.model_dump(exclude_unset=True)
    
    for key, val in resulting_special_condition.items():
        setattr(db_special_condition, key, val)
    

    try:
        await db.commit()
    
    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409, 
            detail="Nombre de condición especial ya está en uso"
        )
    

    await db.refresh(db_special_condition)
    return db_special_condition


async def delete_special_condition(
    special_condition_id: int, 
    db: AsyncSession
) -> None:
    """
    Delete a special condition from the db.

    :param special_condition_id: The ID in the db of the special condition to delete.
    :type special_condition_id: int
    :param db: Database session.
    :type db: AsyncSession
    """

    db_special_condition: SpecialCondition = await get_special_condition_by_id(special_condition_id, db)

    await db.delete(db_special_condition)


    try:
        await db.commit()

    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409,
            detail="La condición especial está en uso y no puede eliminarse"
        )
