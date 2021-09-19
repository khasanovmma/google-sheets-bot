from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅", callback_data="yes"),
        InlineKeyboardButton(text="❌", callback_data="no")
    ]
])