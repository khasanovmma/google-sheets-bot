from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tel_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Jo'natish \ 🇷🇺 Отправить", request_contact=True)
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
