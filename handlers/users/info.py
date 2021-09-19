from aiogram import types
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import state
from aiogram.types import CallbackQuery

from loader import dp, bot
from states import Answer
from utils.write_google import write_google


@dp.callback_query_handler(text="yes", state=["*"])
async def ok(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_name = data.get("last_name")
    first_name = data.get("first_name")
    middle_name = data.get("middle_name")
    phone = data.get("phone")
    write_google(last_name, first_name, middle_name, phone)
    await state.reset_state()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, text="🇺🇿 Siz ro'yxatdan o'tdingiz.\n\n"
                                                   "🇷🇺 Вы прошли регистрацию.")
    await state.reset_state()
    await Answer.info.set()


@dp.message_handler(state=Answer.info)
async def info_reg(message: types.Message):

    await message.answer(text="🇺🇿 Siz ro'yxatdan o'tdingiz.\n\n"
                              "🇷🇺 Вы прошли регистрацию.")
    await Answer.info.set()
