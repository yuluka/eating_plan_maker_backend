from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.config import settings

# Database Engine
engine = create_async_engine(settings.db_url)
SessionLocal = sessionmaker(
    class_=AsyncSession,
    autocommit=False,
    bind=engine,
)


async def get_db():
    """
    Retrieve the database session.

    :yield: The database session.
    :rtype: AsyncSession
    """

    async with SessionLocal() as session:
        yield session
