from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message

from src.locales import ru

router: Router = Router()


async def main(message):
    await message.answer(ru.COMMUNITIES)


@router.message(Command(commands=['communities']))
async def communities_command(message: Message):
    await main(message)


@router.callback_query(F.data == 'communities')
async def communities_inline(callback_query: types.CallbackQuery):
    await main(callback_query.message)
    await callback_query.answer()
