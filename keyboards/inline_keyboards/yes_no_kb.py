from enum import IntEnum, auto
from typing import Optional

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .actions_kb import random_num_updated_cb_data


class YesNo(IntEnum):
    yes = auto()
    no = auto()


class YesNoCallBack(CallbackData, prefix='yes_no'):
    action: YesNo
    param: Optional[str] = None


def build_yes_no_kb(param: str = None) -> InlineKeyboardMarkup:
    print(YesNoCallBack(action=YesNo.yes).pack())
    yes_btn = InlineKeyboardButton(
        text='✅ Да',
        callback_data=YesNoCallBack(action=YesNo.yes, param=param).pack(),
    )
    no_btn = InlineKeyboardButton(
        text='🚫 Нет',
        callback_data=YesNoCallBack(action=YesNo.no, param=param).pack(),
    )
    rows = [[yes_btn, no_btn],]
    markup = InlineKeyboardMarkup(inline_keyboard=rows, )
    return markup
