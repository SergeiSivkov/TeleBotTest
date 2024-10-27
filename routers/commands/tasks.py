from aiogram import types, Router, F
from aiogram.enums import ChatAction
from aiogram.filters import Command

from keyboards.common_keyboards import ButtonText
from keyboards.inline_keyboards.yes_no_kb import build_yes_no_kb

router = Router(name=__name__)


@router.message(Command('tasks', prefix='/!'))
@router.message(F.text.casefold() == ButtonText.MY_TASKS.casefold())
async def seleсt_tasks(message: types.Message):
    await message.answer(
        text=f'Здесь будет выбор из списка заявок',
        reply_markup=build_yes_no_kb(),
    )