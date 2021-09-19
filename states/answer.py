from aiogram.dispatcher.filters.state import StatesGroup, State


class Answer(StatesGroup):
    last_name = State()
    first_name = State()
    middle_name = State()
    phone_number = State()
    info = State()
