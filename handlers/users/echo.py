from aiogram import types

from loader import dp
from filters.shaxsiy_uchun import Shaxsiy

# Echo bot
@dp.message_handler(Shaxsiy())
async def bot_echo(message: types.Message):
    await message.answer(message.text)
