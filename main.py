import asyncio
import logging

from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import config as conf
from DB.fill_db import populate_tasks
from DB.init_db import init_db
from routers import router as main_router


async def set_bot_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/start", description="Начать работу"),
        types.BotCommand(command="/help", description="Помощь"),
        types.BotCommand(command="/menu", description="Показать меню"),
    ]

    # Установка командного меню для бота
    await bot.set_my_commands(commands)


async def main():
    dp = Dispatcher()
    dp.include_router(main_router)

    logging.basicConfig(level=logging.INFO)

    bot = Bot(
        token=conf.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await set_bot_commands(bot)
    await init_db()
    await populate_tasks(15)  # Заполняем 15 задач
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
