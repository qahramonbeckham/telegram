from aiogram import types
from aiogram.types import ContentTypes

from loader import dp


# Echo bot
@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text="Dokument qabul qilindi")
