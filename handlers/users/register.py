from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.menu import tel_btn
from keyboards.inline.inline import inline_btn
from loader import dp, bot
from states.answer import Answer

import re


# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
from utils.write_google import write_google


@dp.message_handler(state=Answer.last_name)
async def answer2(message: types.Message, state: FSMContext):
    last_name = message.text
    await state.update_data(
        {"last_name": last_name}
    )
    await message.answer("""🇺🇿 Ismingizni kriting:

🇷🇺 Введите имя:
""")
    await Answer.next()


@dp.message_handler(state=Answer.first_name)
async def answer3(message: types.Message, state: FSMContext):
    first_name = message.text
    await state.update_data(
        {"first_name": first_name}
    )
    await message.answer("""🇺🇿 Otanizning ismini kriting:

🇷🇺 Введите отчество:
""")
    await Answer.next()


@dp.message_handler(state=Answer.middle_name)
async def answer4(message: types.Message, state: FSMContext):
    middle_name = message.text
    await state.update_data(
        {"middle_name": middle_name}
    )

    await message.answer("""🇺🇿 Telefon raqamingizni yuboring:

🇷🇺 Отправьте номер телефона:
""", reply_markup=tel_btn)
    await Answer.next()


PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


@dp.message_handler(content_types=["contact", "text"], state=Answer.phone_number)
async def answer_phone(message: types.Message, state: FSMContext):

    try:
        number = re.search(PHONE_NUM, message.contact.phone_number)
        if number:
            phone = message.contact.phone_number
            await state.update_data(
                {"phone": phone}
            )

            data = await state.get_data()
            last_name = data.get("last_name")
            first_name = data.get("first_name")
            middle_name = data.get("middle_name")
            phone = data.get("phone")

            msg = "🇺🇿 Quyidagi ma`lumotlar qabul qilindi:\n\n" \
                  "🇷🇺 Следующие данные были приняты:\n\n"
            msg += f"Familiyangiz / Фамилия  - {last_name}\n"
            msg += f"Ismingiz / Имя - {first_name}\n"
            msg += f"Otangiz ismi / Отчество - {middle_name}\n"
            msg += f"Telefon - {phone}\n\n"
            msg += "🇺🇿 Tastiqlash uchun ✅ o'zgartirish uchun ❌ bosing.\n\n"
            msg += "🇷🇺 Выберите кнопку Подтвердить ✅ Изменить ❌."
            # pr
            await bot.delete_message(message.chat.id, message.reply_to_message.message_id)
            await bot.delete_message(message.chat.id, message.message_id)
            await message.answer(msg, reply_markup=inline_btn)
            await state.reset_state(with_data=False)


    except AttributeError:
        number = re.search(PHONE_NUM, message.text)

        if number:
            phone = message.text
            await state.update_data(
                {"phone": phone}
            )

            data = await state.get_data()
            last_name = data.get("last_name")
            first_name = data.get("first_name")
            middle_name = data.get("middle_name")
            phone = data.get("phone")

            msg = "🇺🇿 Quyidagi ma`lumotlar qabul qilindi:\n\n" \
                  "🇷🇺 Следующие данные были приняты:\n\n"
            msg += f"Familiyangiz / Фамилия  - {last_name}\n"
            msg += f"Ismingiz / Имя - {first_name}\n"
            msg += f"Otangiz ismi / Отчество - {middle_name}\n"
            msg += f"Telefon - {phone}\n\n"
            msg += "🇺🇿 Tastiqlash uchun ✅ o'zgartirish uchun ❌ bosing.\n\n"
            msg += "🇷🇺 Выберите кнопку Подтвердить ✅ Изменить ❌."
            await bot.delete_message(message.chat.id, message.message_id - 1)
            await bot.delete_message(message.chat.id, message.message_id)
            await message.answer(msg, reply_markup=inline_btn)

            await state.reset_state(with_data=False)

        else:
            await message.answer("🇺🇿 Telefon raqam kiritilmadi❗️\n\n"
                                 "🇷🇺 Номер телефона не введен❗️")

            await Answer.phone_number.set()


@dp.callback_query_handler(text="no")
async def ok(call: CallbackQuery, state: FSMContext):
    await state.reset_state()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(chat_id=call.from_user.id, text="🇺🇿 Familiyangizni kiriting:\n\n"
                                                           "🇷🇺 Введите фамилию:")
    await Answer.last_name.set()
    await Answer.next()
