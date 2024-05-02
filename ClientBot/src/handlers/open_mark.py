from aiogram import Router, F
from aiogram.types import CallbackQuery

from src.keyboards import open_mark_kb
from src.keyboards.open_subject_kb import OpenMark
from src.locales import ru
from src.models import api

router: Router = Router()


@router.callback_query(OpenMark.filter(F.uuid))
async def main(callback_query: CallbackQuery, callback_data: OpenMark):
    mark = api.get_mark(callback_data.uuid)['data']
    await callback_query.message.edit_text(text=ru.OPEN_MARK.format(subject=mark['subject'], mark=mark['mark'],
                                                                    date=mark['date']),
                                           reply_markup=open_mark_kb.make(mark).as_markup())
