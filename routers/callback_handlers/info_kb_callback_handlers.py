from random import randint

from aiogram import F, Router
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards.yes_no_kb import YesNo, YesNoCallBack

router = Router(name=__name__)


@router.callback_query(
    YesNoCallBack.filter(F.action == YesNo.yes),
)
async def handle_yes_cb(
        callback_query: CallbackQuery,
        callback_data: YesNo,
):
    await callback_query.answer(
        text=f'Ваш выбор ✅: {callback_data}',
        cache_time=4,
    )




@router.callback_query(
    YesNoCallBack.filter(F.action == YesNo.no),
)
async def handle_no_cb(
        callback_query: CallbackQuery,
        callback_data: YesNo,
):
    print('CallBack:', callback_data)
    await callback_query.answer(
        text=f'🚫 Вы выбрали: {callback_data}',
        cache_time=3,
        show_alert=True,
    )
