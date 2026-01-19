from typing import Any, Dict, List, Optional
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.models.micronutrient_group import MicronutrientGroup
from src.schemas.micronutrient_group import MicronutrientGroupCreate, MicronutrientGroupRead, MicronutrientGroupUpdate


async def create_micronutrient_group(
    micronutrient_group: MicronutrientGroupCreate, 
    db: AsyncSession
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

    db_micronutrient_group = MicronutrientGroup(
        name=micronutrient_group.name
    )

    db.add(db_micronutrient_group)
    
    try:
        await db.commit()
    
    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409, 
            detail="Nombre de grupo de micronutrientes ya está en uso"
        )

    await db.refresh(db_micronutrient_group)

    return db_micronutrient_group


async def get_all_micronutrient_groups(
    db: AsyncSession
) -> List[MicronutrientGroupRead]:
    """
    Retrieve all micronutrient groups from the database.

    :param db: Database session.
    :type db: AsyncSession
    :return: A list with all the micronutrient groups found.
    :rtype: List[MicronutrientGroupRead]
    """

    result = await db.execute(
        select(MicronutrientGroup)
    )

    db_micronutrient_groups: List[MicronutrientGroup] = result.scalars().all()

    return db_micronutrient_groups


async def get_micronutrient_group_by_id(
    micronutrient_group_id: int,
    db: AsyncSession
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

    result = await db.execute(
        select(MicronutrientGroup).where(MicronutrientGroup.id == micronutrient_group_id)
    )

    db_micronutrient_group: Optional[MicronutrientGroup] = result.scalar_one_or_none()

    if not db_micronutrient_group:
        raise HTTPException(status_code=404, detail="Grupo de micronutrientes no encontrado")

    return db_micronutrient_group


async def update_micronutrient_group(
    micronutrient_group_id: int,
    micronutrient_group_update: MicronutrientGroupUpdate,
    db: AsyncSession
) -> MicronutrientGroupRead:
    """
    Update a micronutrient group into the db.

    :param micronutrient_group_id: The ID in the db of the micronutrient group to update.
    :type micronutrient_group_id: int
    :param micronutrient_group_update: The information to update the micronutrient group.
    :type micronutrient_group_update: MicronutrientGroupUpdate
    :param db: Database session.
    :type db: AsyncSession
    :return: The updated micronutrient group.
    :rtype: MicronutrientGroupRead
    :raises HTTPException: If the used name is already in use or if the micronutrient group is not found.
    """

    db_micronutrient_group: MicronutrientGroup = await get_micronutrient_group_by_id(micronutrient_group_id, db)

    resulting_micronutrient_group: Dict[str, Any] = micronutrient_group_update.model_dump(exclude_unset=True)
    
    for key, val in resulting_micronutrient_group.items():
        setattr(db_micronutrient_group, key, val)
    

    try:
        await db.commit()
    
    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409, 
            detail="Nombre de grupo de micronutrientes ya está en uso"
        )
    

    await db.refresh(db_micronutrient_group)
    return db_micronutrient_group


async def delete_micronutrient_group(
    micronutrient_group_id: int, 
    db: AsyncSession
) -> None:
    """
    Delete a micronutrient group from the db.

    :param micronutrient_group_id: The ID in the db of the micronutrient group to delete.
    :type micronutrient_group_id: int
    :param db: Database session.
    :type db: AsyncSession
    """

    db_micronutrient_group: MicronutrientGroup = await get_micronutrient_group_by_id(micronutrient_group_id, db)

    await db.delete(db_micronutrient_group)


    try:
        await db.commit()

    except IntegrityError:
        await db.rollback()

        raise HTTPException(
            status_code=409,
            detail="El grupo de micronutrientes está en uso y no puede eliminarse"
        )
