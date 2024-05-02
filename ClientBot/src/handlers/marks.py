from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message

from src.keyboards import marks_kb
from src.locales import ru
from src.models import api

router: Router = Router()


async def main(message, inline=False):
    marks = api.get_marks(message.chat.id)['data']

    message_text = ru.MARKS
    message_kb = marks_kb.make(marks).as_markup()

    if not inline:
        await message.reply(text=message_text, reply_markup=message_kb)
    else:
        await message.edit_text(text=message_text, reply_markup=message_kb)


@router.message(Command(commands=['marks']))
async def start_command(message: Message):
    await main(message)


@router.callback_query(F.data == 'marks')
async def start_inline(callback_query: types.CallbackQuery):
    await main(callback_query.message, inline=True)
    await callback_query.answer()
