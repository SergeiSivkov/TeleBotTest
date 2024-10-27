from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import (
    sessionmaker, declarative_base, declared_attr, mapped_column,
)

DATABASE_URL = "sqlite+aiosqlite:///./test.db"


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String)
    is_active = mapped_column(Boolean, nullable=False, default=True)
    created_at = mapped_column(
        DateTime(timezone=True), server_default=func.now(),
    )
    last_active_at = mapped_column(
        DateTime(timezone=True), onupdate=func.now(),
    )


engine = create_async_engine(DATABASE_URL, echo=True)

# Создаем базовый класс для моделей
Base = declarative_base(cls=PreBase)

# Создаем фабрику сессий
async_session = sessionmaker(engine, class_=AsyncSession)


