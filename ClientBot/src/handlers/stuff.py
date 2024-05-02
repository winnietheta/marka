from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message

from src.locales import ru

router: Router = Router()


async def main(message):
    await message.answer(ru.STUFF)


@router.message(Command(commands=['stuff']))
async def start_command(message: Message):
    await main(message)


@router.callback_query(F.data == 'stuff')
async def start_inline(callback_query: types.CallbackQuery):
    await main(callback_query.message)
    await callback_query.answer()
