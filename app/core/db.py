from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from typing import AsyncGenerator


Base = declarative_base()
engine = create_async_engine("postgresql+asyncpg://postgres:moh4mm4d580@localhost:5432/fastapi_db", echo=True, future=True)

async def init_db():
    """ Create a connection to our db """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session