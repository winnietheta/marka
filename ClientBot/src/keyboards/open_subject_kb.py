from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class OpenMark(CallbackData, prefix="open_mark"):
    uuid: str


def make(marks):
    builder = InlineKeyboardBuilder()

    for value in marks:
        builder.row(InlineKeyboardButton(text=value['mark'] + ' - ' + value['date'],
                                         callback_data=OpenMark(uuid=value['uuid']).pack()))

    builder.row(InlineKeyboardButton(text='◀️ Назад к оценкам', callback_data='marks'))

    return builder
