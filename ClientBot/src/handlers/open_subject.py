from aiogram import Router, F
from aiogram.types import CallbackQuery

from src.keyboards import open_subject_kb
from src.keyboards.marks_kb import OpenSubject
from src.locales import ru
from src.models import api

router: Router = Router()


@router.callback_query(OpenSubject.filter(F.subject))
async def main(callback_query: CallbackQuery, callback_data: OpenSubject):
    marks = api.get_marks(callback_query.message.chat.id)['data'][callback_data.subject]
    required_marks = ''

    if 4.50 > float(marks['average']) >= 3.50:
        required_marks = '❗️До балла 4.50 осталось ' + str(marks['required_five_to_4.50']) + ' "5"'
    if 3.50 > float(marks['average']) >= 2.50:
        required_marks = '❗️До балла 3.50 осталось ' + str(marks['required_five_to_3.50']) + ' "5" или ' + str(
            marks['required_four_to_3.50']) + ' "4"'
    if float(marks['average']) < 2.50:
        required_marks = '❗️До балла 2.50 осталось ' + str(marks['required_five_to_2.50']) + ' "5" или ' + str(
            marks['required_four_to_2.50']) + ' "4" или ' + str(marks['required_three_to_2.50']) + ' "3"'

    await callback_query.message.edit_text(
        text=ru.OPEN_SUBJECT.format(subject=callback_data.subject, average=marks['average'],
                                    required_marks=required_marks),
        reply_markup=open_subject_kb.make(marks['marks']).as_markup())
