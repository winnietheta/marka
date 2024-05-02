from aiogram import Router, F
from aiogram.types import CallbackQuery

from src.keyboards.open_mark_kb import DeleteMark
from src.locales import ru
from src.models import api

router: Router = Router()


@router.callback_query(DeleteMark.filter(F.uuid))
async def main(callback_query: CallbackQuery, callback_data: DeleteMark):
    res = api.delete_mark(callback_data.uuid)['data']
    await callback_query.message.delete()
    await callback_query.message.answer(ru.MARK_DELETED)
