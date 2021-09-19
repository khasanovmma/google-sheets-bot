from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsPrivate
from loader import dp
from states.answer import Answer


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.delete()
    await message.answer(f"""🇺🇿 Assalomu aleykum, ro'yxatdan o'tishni boshlaymiz.
Familiyangizni kiriting:\n
🇷🇺 Здравствуйте, начнем регистрацию.
Введите фамилию:
""")
    await Answer.last_name.set()
