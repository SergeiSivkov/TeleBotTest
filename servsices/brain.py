from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from DB.models import User
from DB import async_session


async def check_new_user(
        tg_id: int,
        # session: AsyncSession = async_session(),
):
    '''Ищем пользователя по Telegram ID. '''

    async with async_session() as session:

        quote = await session.execute(select(User).filter_by(tgid=tg_id))
        user = quote.scalars().first()
        if user:
            return user
        else:
            # Если пользователь не найден, создаем его
            new_user = User(
                tgid=tg_id,
                name='Новый пользователь',
                is_active=True,
            )
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user
