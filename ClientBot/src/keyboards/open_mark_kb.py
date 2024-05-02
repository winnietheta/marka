from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.keyboards.marks_kb import OpenSubject


class DeleteMark(CallbackData, prefix="delete_mark"):
    uuid: str


def make(mark):
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text='🗑 Удалить',
                                     callback_data=DeleteMark(uuid=mark['uuid']).pack()))
    builder.row(
        InlineKeyboardButton(text='◀️ Назад к предмету', callback_data=OpenSubject(subject=mark['subject']).pack()))

    return builder
