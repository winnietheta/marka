from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message

from src.keyboards import start_main_kb
from src.locales import ru
from src.models import api

router: Router = Router()


async def main(message, inline=False):
    marks = api.get_marks(message.chat.id)['data']
    attention = ''

    if len(marks) > 0:
        for key, value in marks.items():
            if float(value['average']) < 2.60:
                attention += '❗️' + key + ' - ' + str(value['average'] + '\n')

    message_text = ru.START.format(attention=attention)
    message_kb = start_main_kb.make().as_markup()

    if not inline:
        await message.reply(text=message_text, reply_markup=message_kb)
    else:
        await message.edit_text(text=message_text, reply_markup=message_kb)


@router.message(Command(commands=['start']))
async def start_command(message: Message):
    await main(message)


@router.callback_query(F.data == 'start')
async def start_inline(callback_query: types.CallbackQuery):
    await main(callback_query.message, inline=True)
    await callback_query.answer()
