from aiogram.fsm.state import StatesGroup, State


class AddMark(StatesGroup):
    subject = State()
    mark = State()
    date = State()
