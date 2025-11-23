from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession 
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker
from .settings import *
import os

DATABASE_URL = AppSettings().database_url


async_session = sessionmaker(  # type: ignore[call-overload]
    create_async_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        pool_size=50,
        max_overflow=100,
        pool_timeout=30,
        pool_recycle=1800,
        pool_use_lifo=True,
    ),
    expire_on_commit=False,
    class_=AsyncSession,
)


class AsyncDBContextManager:
    def __init__(self) -> None:
        print(DATABASE_URL)
        session = sessionmaker( 
            create_async_engine(DATABASE_URL, pool_pre_ping=True),
            expire_on_commit=False,
            class_=AsyncSession,
            autoflush = True
        )
        self.db = session()

    async def __aenter__(self) -> Any:
        return self.db

    async def __aexit__(self, *exc: Any) -> Any:
        await self.db.close() 

async def get_db():
    db = async_session()
    try:
            yield db
    finally:
            await db.close()