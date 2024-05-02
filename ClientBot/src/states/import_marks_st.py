from aiogram.fsm.state import StatesGroup, State


class ImportMarks(StatesGroup):
    session_id = State()
