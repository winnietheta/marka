from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from src.locales import ru
from src.models import api
from src.states.import_marks_st import ImportMarks

router: Router = Router()


@router.callback_query(F.data == 'import_marks')
async def main(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.reply(text=ru.IMPORT_MARKS_1)
    await state.set_state(ImportMarks.session_id)

    await callback_query.answer()


@router.message(ImportMarks.session_id)
async def session_id_input(message: types.Message, state: FSMContext):
    await state.clear()

    if not api.import_marks(message.chat.id, message.text)['status']:
        await message.reply(text=ru.IMPORT_MARKS_FAILED)
        return

    await message.reply(text=ru.IMPORT_MARKS_2)
