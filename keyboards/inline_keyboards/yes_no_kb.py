from enum import Enum

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .actions_kb import random_num_updated_cb_data


class RandomNumAction(Enum):
    dice = "dice"
    modal = "modal"


class RandomNumCbData(CallbackData, prefix="random_num"):
    action: RandomNumAction


def build_yes_no_kb() -> InlineKeyboardMarkup:
    yes_btn = InlineKeyboardButton(
        text='✅ Да',
        callback_data=RandomNumCbData(action=RandomNumAction.modal).pack(),
    )
    no_btn = InlineKeyboardButton(
        text="💬 Нет",
        callback_data=RandomNumCbData(action=RandomNumAction.modal).pack(),
    )
    bot_source_code_btn = InlineKeyboardButton(
        text="🤖 Исходный код этого бота",
        url="https://github.com/mahenzon/demo-tg-bot",
    )
    btn_random_site = InlineKeyboardButton(
        text="Random number message",
        callback_data=random_num_updated_cb_data,
    )
    btn_random_num = InlineKeyboardButton(
        text="🎲 Random Num",
        callback_data=RandomNumCbData(action=RandomNumAction.dice).pack(),
    )
    btn_random_num_modal = InlineKeyboardButton(
        text="👾 Random Number",
        callback_data=RandomNumCbData(action=RandomNumAction.modal).pack(),
    )
    row_tg = [yes_btn, no_btn]
    rows = [
        row_tg,
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
