import time

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from src.keyboards import add_mark_kb
from src.locales import ru
from src.models import api
from src.states.add_mark_st import AddMark

router: Router = Router()


@router.callback_query(F.data == 'add_mark')
async def main(callback_query: types.CallbackQuery, state: FSMContext):
    marks = api.get_marks(callback_query.message.chat.id)['data']
    await callback_query.message.reply(text=ru.NEW_MARK_1, reply_markup=add_mark_kb.make(marks).as_markup())
    await state.set_state(AddMark.subject)
    await callback_query.answer()


@router.message(AddMark.subject)
async def subject_input(message: types.Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await state.set_state(AddMark.mark)
    await message.reply(text=ru.NEW_MARK_2, reply_markup=add_mark_kb.marks().as_markup())


@router.message(AddMark.mark)
async def mark_input(message: types.Message, state: FSMContext):
    if message.text == '5' or message.text == '4' or message.text == '3' or message.text == '2' or message.text == '1':
        await state.update_data(mark=message.text)
        await state.set_state(AddMark.date)
        await message.reply(text=ru.NEW_MARK_3, reply_markup=add_mark_kb.dates().as_markup())
    else:
        await message.reply(text=ru.INVALID_MARK)


@router.message(AddMark.date)
async def date_input(message: types.Message, state: FSMContext):
    try:
        time.strptime(message.text, '%d.%m.%Y')
    except ValueError:
        await message.reply(text=ru.INVALID_DATE)
        return

    await state.update_data(date=message.text)
    data = await state.get_data()

    api.add_mark(message.chat.id, data['subject'], data['mark'], data['date'])

    await state.clear()
    await message.reply(text=ru.NEW_MARK_4, reply_markup=ReplyKeyboardRemove())
