from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class OpenSubject(CallbackData, prefix="open_subject"):
    subject: str


def make(marks):
    builder = InlineKeyboardBuilder()

    if len(marks) > 0:
        for key, value in marks.items():
            builder.row(InlineKeyboardButton(text=key + ' - ' + str(value['average']),
                                             callback_data=OpenSubject(subject=key).pack()))
    else:
        builder.row(InlineKeyboardButton(text='Время добавить первую оценку!', callback_data='x'))

    builder.row(InlineKeyboardButton(text='➕ Добавить оценку', callback_data='add_mark'))
    builder.row(InlineKeyboardButton(text='🗑 Сбросить все оценки', callback_data='reset_marks'))
    builder.row(InlineKeyboardButton(text='◀️ Назад в меню', callback_data='start'))

    return builder
