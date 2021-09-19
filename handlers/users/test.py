from aiogram import types

from data.config import ADMINS
from loader import dp


@dp.message_handler(commands=["test"])
async def bot_help(message: types.Message):
    if str(message.chat.id) in ADMINS:
        await message.answer('Bot ishlavotdi✅')
