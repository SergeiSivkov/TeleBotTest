from aiogram import Router, types

router = Router(name=__name__)


@router.message()
async def echo_message(message: types.Message):
    # if message.text:
    #     await message.answer(text='Wait please ...')
    #     await message.reply(text=message.text)
    # elif message.sticker:
    #     await message.reply_sticker(sticker=message.sticker.file_id)
    # else:
    #     await message.reply(text='жду информации... 🧐')
    try:
        await message.send_copy(
            chat_id=message.chat.id,
            reply_to_message_id=message.message_id,
        )
    except TypeError:
        await message.reply(text='жду информации... 🧐')
