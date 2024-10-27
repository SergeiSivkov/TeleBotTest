from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command

# from DB import get_async_session
from keyboards.common_keyboards import get_on_start_kb, ButtonText
from keyboards.inline_keyboards import yes_no_kb
from servsices.brain import check_new_user

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    user = await check_new_user(message.from_user.id)
    if not user.is_active:
        await message.answer(
            text=f'Уважаемый {message.from_user.full_name}! \n '
                 f'Ваша запись заблокирована обратитесь к администратору \n',
            # reply_markup=get_on_start_kb(),
        )
    else:
        await message.answer(
            text=f'Привет, {user.name}! \n #начало',
            reply_markup=get_on_start_kb(),
        )


@router.message(F.text == ButtonText.HELP)
@router.message(Command('help'))
async def handle_help(message: types.Message):
    help_text = 'я бот помошник.\n вот что я умею 👇:\n'
    await message.answer(text=help_text + str(message.message_id))
