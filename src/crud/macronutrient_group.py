from typing import Any, Dict, List, Optional
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.models.macronutrient_group import MacronutrientGroup
from src.schemas.macronutrient_group import MacronutrientGroupCreate, MacronutrientGroupRead, MacronutrientGroupUpdate


async def create_macronutrient_group(
    macronutrient_group: MacronutrientGroupCreate, 
    db: AsyncSession
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

    db_macronutrient_group = MacronutrientGroup(
        name=macronutrient_group.name
    )

    db.add(db_macronutrient_group)
    
    try:
        await db.commit()
    
    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409, 
            detail="Nombre de grupo de macronutrientes ya está en uso"
        )

    await db.refresh(db_macronutrient_group)

    return db_macronutrient_group


async def get_all_macronutrient_groups(
    db: AsyncSession
) -> List[MacronutrientGroupRead]:
    """
    Retrieve all macronutrient groups from the database.

    :param db: Database session.
    :type db: AsyncSession
    :return: A list with all the macronutrient groups found.
    :rtype: List[MacronutrientGroupRead]
    """

    result = await db.execute(
        select(MacronutrientGroup)
    )

    db_macronutrient_groups: List[MacronutrientGroup] = result.scalars().all()

    return db_macronutrient_groups


async def get_macronutrient_group_by_id(
    macronutrient_group_id: int,
    db: AsyncSession
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

    result = await db.execute(
        select(MacronutrientGroup).where(MacronutrientGroup.id == macronutrient_group_id)
    )

    db_macronutrient_group: Optional[MacronutrientGroup] = result.scalar_one_or_none()

    if not db_macronutrient_group:
        raise HTTPException(status_code=404, detail="Grupo de macronutrientes no encontrado")

    return db_macronutrient_group


async def update_macronutrient_group(
    macronutrient_group_id: int,
    macronutrient_group_update: MacronutrientGroupUpdate,
    db: AsyncSession
) -> MacronutrientGroupRead:
    """
    Update a macronutrient group into the db.

    :param macronutrient_group_id: The ID in the db of the macronutrient group to update.
    :type macronutrient_group_id: int
    :param macronutrient_group_update: The information to update the macronutrient group.
    :type macronutrient_group_update: MacronutrientGroupUpdate
    :param db: Database session.
    :type db: AsyncSession
    :return: The updated macronutrient group.
    :rtype: MacronutrientGroupRead
    :raises HTTPException: If the used name is already in use or if the macronutrient group is not found.
    """

    db_macronutrient_group: MacronutrientGroup = await get_macronutrient_group_by_id(macronutrient_group_id, db)

    resulting_macronutrient_group: Dict[str, Any] = macronutrient_group_update.model_dump(exclude_unset=True)
    
    for key, val in resulting_macronutrient_group.items():
        setattr(db_macronutrient_group, key, val)
    

    try:
        await db.commit()
    
    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409, 
            detail="Nombre de grupo de macronutrientes ya está en uso"
        )
    

    await db.refresh(db_macronutrient_group)
    return db_macronutrient_group


async def delete_macronutrient_group(
    macronutrient_group_id: int, 
    db: AsyncSession
) -> None:
    """
    Delete a macronutrient group from the db.

    :param macronutrient_group_id: The ID in the db of the macronutrient group to delete.
    :type macronutrient_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    """

    db_macronutrient_group: MacronutrientGroup = await get_macronutrient_group_by_id(macronutrient_group_id, db)

    await db.delete(db_macronutrient_group)


    try:
        await db.commit()

    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409,
            detail="El grupo de macronutrientes está en uso y no puede eliminarse"
        )
