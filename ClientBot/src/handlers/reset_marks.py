from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message

from src.locales import ru
from src.models import api

router: Router = Router()


async def main(message, inline=False):
    api.reset_marks(message.chat.id)
    message_text = ru.MARKS_RESET

    if not inline:
        await message.reply(text=message_text)
    else:
        await message.edit_text(text=message_text)


@router.message(Command(commands=['reset_marks']))
async def start_command(message: Message):
    await main(message)


@router.callback_query(F.data == 'reset_marks')
async def start_inline(callback_query: types.CallbackQuery):
    await main(callback_query.message, inline=True)
    await callback_query.answer()
