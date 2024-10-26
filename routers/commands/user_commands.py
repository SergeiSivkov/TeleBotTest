import io

from aiogram import types, Router
from aiogram.enums import ChatAction
from aiogram.filters import Command

from keyboards.common_keyboards import ButtonText

router = Router(name=__name__)


@router.message(Command("file"))
async def handle_command_file(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    file_path = "/Users/sivkov/Downloads/IMG_0B8D7D2D5639-1.jpeg"
    await message.reply_document(
        document=types.FSInputFile(
            path=file_path,
            filename="Camnal_Bag.jpeg",
        ),
        caption='#файл',
    )


@router.message(Command("text"))
async def send_txt_file(message: types.Message):
    file = io.StringIO()
    file.write("Hello, world!\n")
    file.write("This is a text file.\n")
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode("utf-8"),
            filename="text.txt",
        ),
    )



@router.message(Command('tasks', prefix='/!'))
async def selekt_tasks(message: types.Message):
    pass


@router.message(Command('newtask', prefix='/!'))
@router.message(F.text.casefold() == ButtonText.NEW_TASK)
async def selekt_tasks(message: types.Message):
    pass