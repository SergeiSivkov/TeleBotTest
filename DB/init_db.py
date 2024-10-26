from .database import engine, Base

async def init_db():
    from DB.models import User  # noqa

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
